from django.views.generic import ListView

from ...backend.home.models import Config
from ...backend.profiles.models import Profile
from ...backend.resume.models import *


# Create your views here.

class HomeView(ListView):
    model = Config
    template_name = "frontend/home/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['profile'] = Profile.objects.filter(status=True).first()
        context['skills'] = Skill.objects.filter(status=True).all()
        context['experiences'] = Experience.objects.filter(status=True, type='text').all()
        context['experienceNumbers'] = Experience.objects.filter(status=True, type='number').all()
        context['educations'] = Education.objects.filter(status=True).all()

        return context
