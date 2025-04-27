from lib2to3.fixes.fix_input import context

import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import JobApply


class Index(ListView):
    model = JobApply
    template_name = "backend/jobs/job_list.html"


def format_phone_number(number):
    try:
        number = str(int(number))
        formatted_number = f"{number[1:4]}{number[4:7]}{number[7:]}"
        return formatted_number
    except Exception as e:
        return None


def job_upload(request):
    if request.method == "POST":
        excel_file = request.FILES.get('file')
        if not excel_file.name.endswith('.xlsx'):
            messages.error(request, 'Please upload an Excel file.')
            return redirect('job_upload')

        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            JobApply.objects.get_or_create(
                phone_number=format_phone_number(row.get('phone_number')),
                defaults={
                    'name': row.get('name'),
                    'full_address': row.get('full_address'),
                    'latitude': row.get('latitude'),
                    'longitude': row.get('longitude'),
                    'review_count': row.get('review_count'),
                    'rating': row.get('rating'),
                    'timezone': row.get('timezone'),
                    'website': row.get('website'),
                    'place_id': row.get('place_id'),
                    'place_link': row.get('place_link'),
                    'types': row.get('types'),
                    'price_level': row.get('price_level'),
                    'sunday': row.get('Sunday'),
                    'monday': row.get('Monday'),
                    'tuesday': row.get('Tuesday'),
                    'wednesday': row.get('Wednesday'),
                    'thursday': row.get('Thursday'),
                    'friday': row.get('Friday'),
                    'saturday': row.get('Saturday'),
                    'city': row.get('city'),
                    'state': row.get('state'),
                    'verified': row.get('verified') == True or row.get('verified') == "TRUE",
                    'photos': row.get('photos'),
                    'description': row.get('description'),
                }
            )
        messages.success(request, 'Jobs uploaded successfully.')
        return redirect('jobApply:job_list')

    return render(request, 'backend/jobs/job_upload.html')

def sms_upload(request):
    if request.method == "POST":
        sms = request.POST.get('sms')

        JobApply.objects.update(sms=sms)

        messages.success(request, 'SMS updated successfully.')
        return redirect('jobApply:sms_upload')
    context = {
        'sms': JobApply.objects.first().sms
    }
    return render(request, 'backend/jobs/sms_upload.html', context)


def apply_job(request, job_id):
    job = get_object_or_404(JobApply, id=job_id)
    job.status = 'applied'
    job.save()
    messages.success(request, f"You have successfully applied for {job.name}.")
    return redirect('jobApply:job_list')


def apply_job_response(request, job_id):
    job = get_object_or_404(JobApply, id=job_id)
    job.status = 'got_response'
    job.save()
    messages.success(request, f"You have successfully updated for {job.name}.")
    return redirect('jobApply:job_list')
