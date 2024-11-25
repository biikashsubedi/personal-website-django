from django.urls import path
from .views import *

app_name = 'contactUs'
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
