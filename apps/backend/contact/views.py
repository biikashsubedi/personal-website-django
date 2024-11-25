from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import ContactUsForm


class Index(ListView):
    model = ContactUs
    template_name = "backend/contactUs/index.html"
