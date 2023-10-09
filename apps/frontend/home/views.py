from django.views.generic import ListView

from ...backend.home.models import Config


# Create your views here.

class HomeView(ListView):
    model = Config
    template_name = "frontend/home/index.html"
