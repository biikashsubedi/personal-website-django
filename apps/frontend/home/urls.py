from django.urls import path
from .views import *

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('profile', ResumeView.as_view(), name='resume'),
    path('works', WorksView.as_view(), name='works'),
    path('blogs', BlogView.as_view(), name='blogs'),
    path('contact', ContactView.as_view(), name='contact'),
    path('contact-us/store/', store_contact_us, name='store_contact_us'),
]
