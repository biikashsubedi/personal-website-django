from django.views.generic import ListView

from ...backend.home.models import Home


# Create your views here.

class HomeView(ListView):
    model = Home
    template_name = "frontend/home/index.html"
