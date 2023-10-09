from django.urls import path
from .views import *

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
