from django.views.generic import ListView

from apps.backend.profiles.models import Profile


# Car category
class Index(ListView):
    model = Profile
    template_name = "backend/portfolio/index.html"
