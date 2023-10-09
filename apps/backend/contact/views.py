from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import ContactUsForm


class Create(SuccessMessageMixin, CreateView):
    model = ContactUs
    template_name = "backend/contactUs/form.html"
    form_class = ContactUsForm
    success_message = "Thanks for your message."
    success_url = reverse_lazy('home:index')
