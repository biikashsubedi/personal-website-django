from django.urls import path
from .views import *

app_name = 'analytic'
urlpatterns = [
    path('most/used/device/reset/', resetDeviceApiAnalytic, name='most.used.device.reset'),
]
