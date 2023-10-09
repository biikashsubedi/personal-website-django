from django.shortcuts import render
from .models import *
from django.views.generic import ListView


# Create your views here.

class HomeView(ListView):
    model = Home
    template_name = "backend/home/index.html"
