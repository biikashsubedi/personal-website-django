from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from ..profiles.models import Profile


# Create your views here.

class HomeView(ListView):
    model = Config
    template_name = "backend/home/index.html"
