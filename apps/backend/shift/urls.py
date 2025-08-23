from django.urls import path
from .views import *

app_name = 'shift'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('checkin/', checkin, name='checkin'),
    path('checkout/<int:attendance_id>/', checkout, name='checkout'),
path('history/', history, name='history')

]
