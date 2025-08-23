import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
from datetime import datetime
from django.utils import timezone


class Index(ListView):
    model = Attendance
    template_name = "backend/shift/shift.html"


@csrf_exempt
def checkin(request):
    # --- GET: check pending attendance for today ---
    if request.method == 'GET' and request.GET.get('today_only'):
        today = timezone.localdate()
        pending = Attendance.objects.filter(
            checkin_time__date=today,
            checkout_time__isnull=True
        ).first()
        if pending:
            return JsonResponse({'pending': {'id': pending.id, 'checkout_time': pending.checkout_time}})
        return JsonResponse({'pending': None})

    # --- POST: create a new check-in ---
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        checkin_time = data.get('checkin_time')
        if checkin_time:
            checkin_time = datetime.fromisoformat(checkin_time)
        else:
            checkin_time = timezone.now()

        # dd(checkin_time)

        # Prevent multiple check-ins per day
        today = checkin_time.date()
        already = Attendance.objects.filter(checkin_time__date=today).exists()
        if already:
            return JsonResponse({'error': 'Already checked in today'}, status=400)

        attendance = Attendance.objects.create(
            checkin_time=checkin_time
        )

        return JsonResponse({
            'id': attendance.id,
            'checkin_time': attendance.checkin_time.isoformat()
        })

    # --- Any other method ---
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def checkout(request, attendance_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        try:
            attendance = Attendance.objects.get(id=attendance_id)
        except Attendance.DoesNotExist:
            return JsonResponse({'error': 'Attendance not found'}, status=404)

        checkin_time = data.get('checkin_time')
        checkout_time = data.get('checkout_time')
        if checkout_time:
            # Convert to timezone-aware datetime
            checkout_time = timezone.make_aware(datetime.fromisoformat(checkout_time))
        else:
            checkout_time = None


        if checkin_time:
            # Convert to timezone-aware datetime
            checkin_time = timezone.make_aware(datetime.fromisoformat(checkin_time))
        else:
            checkin_time = attendance.checkin_time

        attendance.checkin_time = checkin_time
        attendance.checkout_time = checkout_time
        attendance.status = 'checked_out'
        attendance.save()

        return JsonResponse({
            'id': attendance.id,
            'checkin_time': checkin_time.isoformat(),
            'checkout_time': attendance.checkout_time.isoformat() if checkout_time else None,
            'hours_worked': attendance.hours_worked,
            'total_pay': attendance.total_pay,
            'status': attendance.status
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def history(request):
    date_str = request.GET.get('date')
    if date_str:
        date = timezone.datetime.fromisoformat(date_str).date()
    else:
        date = timezone.localdate()

    records = Attendance.objects.filter(checkin_time__date=date)
    data = []
    for r in records:
        data.append({
            'id': r.id,
            'checkin_time': r.checkin_time.isoformat() if r.checkin_time else '',
            'checkout_time': r.checkout_time.isoformat() if r.checkout_time else '',
            'total_pay': r.total_pay
        })
    return JsonResponse({'records': data})