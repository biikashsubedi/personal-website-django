from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),

    path('profile/data', profileData, name='profile.data'),
    path('skill/data', skillData, name='skill.data'),
    path('education/data', educationData, name='education.data'),
    path('experience/data', experienceData, name='experience.data'),
]
