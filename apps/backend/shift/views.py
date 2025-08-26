import json
from django.utils.timezone import make_aware
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from pytz import timezone as tzz
from .models import Shift
from datetime import datetime, timedelta


class Index(ListView):
    model = Shift
    template_name = "backend/shift/shift.html"


@csrf_exempt
def checkin(request):
    # --- GET: check pending shift for today ---
    if request.method == 'GET' and request.GET.get('today_only'):
        today = timezone.localdate()
        pending = Shift.objects.filter(
            date=today,
            status='checked_in'
        ).first()
        if pending:
            return JsonResponse({'pending': {'id': pending.id, 'checkout_time': str(pending.checkout_time)}})
        return JsonResponse({'pending': None})

    # --- POST: create a new check-in ---
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        checkin_time = data.get('checkin_time')
        if checkin_time:
            checkin_time = datetime.fromisoformat(checkin_time).time()
        else:
            checkin_time = timezone.localtime().time()

        today = timezone.localdate()

        # Prevent multiple check-ins per day
        already = Shift.objects.filter(date=today).exists()
        if already:
            return JsonResponse({'error': 'Already checked in today'}, status=400)

        shift = Shift.objects.create(
            date=today,
            checkin_time=checkin_time,
            status='checked_in'
        )

        return JsonResponse({
            'id': shift.id,
            'date': str(shift.date),
            'checkin_time': shift.checkin_time.strftime("%H:%M"),
            'status': shift.status
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def checkout(request, shift_id):
    if request.method == "POST":
        try:
            # Handle JSON or form data
            if request.content_type == "application/json":
                payload = json.loads(request.body.decode("utf-8"))
            else:
                payload = request.POST

            checkout_time_str = payload.get("checkout_time")
            if checkout_time_str:
                # Parse datetime
                checkout_time = datetime.fromisoformat(checkout_time_str)

                shift = Shift.objects.get(pk=shift_id)

                # Combine with date for duration calc
                checkin_dt = datetime.combine(shift.date, shift.checkin_time)
                checkout_dt = datetime.combine(shift.date, checkout_time.time())

                # Handle overnight case
                if checkout_dt < checkin_dt:
                    checkout_dt += timedelta(days=1)

                # Duration
                duration = checkout_dt - checkin_dt

                shift.checkout_time = checkout_time.time()
                shift.status = "checked_out"
                shift.save()

                return JsonResponse({
                    'id': shift.id,
                    'date': str(shift.date),
                    'checkin_time': shift.checkin_time.strftime("%H:%M"),
                    'checkout_time': shift.checkout_time.strftime("%H:%M") if shift.checkout_time else None,
                    'hours_worked': round(duration.total_seconds() / 3600, 2),
                    'total_pay': round(duration.total_seconds() / 3600 * shift.HOURLY_RATE, 2),
                    'status': shift.status
                })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)




def history(request):
    date_str = request.GET.get('date')
    if date_str:
        date = datetime.fromisoformat(date_str).date()
    else:
        date = timezone.localdate()

    records = Shift.objects.filter(date=date)
    data = []
    for r in records:
        data.append({
            'id': r.id,
            'date': str(r.date),
            'checkin_time': r.checkin_time.strftime("%H:%M") if r.checkin_time else '',
            'checkout_time': r.checkout_time.strftime("%H:%M") if r.checkout_time else '',
            'total_pay': r.total_pay
        })
    return JsonResponse({'records': data})
