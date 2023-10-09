from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import ApiKeyForm


# Car category
class Index(ListView):
    model = ApiKey
    template_name = "backend/apikey/index.html"


class Create(SuccessMessageMixin, CreateView):
    model = ApiKey
    template_name = "backend/apikey/form.html"
    form_class = ApiKeyForm
    success_message = "ApiKey Created Successfully."
    success_url = reverse_lazy('apikey:index')


class Update(SuccessMessageMixin, UpdateView):
    model = ApiKey
    template_name = "backend/apikey/form.html"
    form_class = ApiKeyForm
    success_message = "ApiKey Updated Successfully."
    success_url = reverse_lazy('apikey:index')


class Delete(SuccessMessageMixin, DeleteView):
    model = ApiKey
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "ApiKey Deleted Successfully."
    success_url = reverse_lazy('apikey:index')
