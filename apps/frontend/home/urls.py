from django.urls import path
from .views import *

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('resume', HomeView.as_view(), name='resume'),
    path('works', HomeView.as_view(), name='works'),
    path('blogs', HomeView.as_view(), name='blogs'),
    path('contact', HomeView.as_view(), name='contact'),
]
