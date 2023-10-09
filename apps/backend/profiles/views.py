from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import ProfileForm


# Car category
class Index(ListView):
    model = Profile
    template_name = "backend/profile/index.html"


class Create(SuccessMessageMixin, CreateView):
    model = Profile
    template_name = "backend/profile/form.html"
    form_class = ProfileForm
    success_message = "Profile Created Successfully."
    success_url = reverse_lazy('profile:index')


class Update(SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = "backend/profile/form.html"
    form_class = ProfileForm
    success_message = "Profile Updated Successfully."
    success_url = reverse_lazy('profile:index')


class Delete(SuccessMessageMixin, DeleteView):
    model = Profile
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Profile Deleted Successfully."
    success_url = reverse_lazy('profile:index')
