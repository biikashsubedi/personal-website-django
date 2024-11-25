from .models import *
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect


def resetDeviceApiAnalytic(request):
    DeviceAnalytic.objects.all().delete()
    messages.success(request, 'Successfully data reset.')
    return redirect(reverse('config:index'))