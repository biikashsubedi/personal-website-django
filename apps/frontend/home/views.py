from django.views.generic import ListView

from personalPortfoloi.metaData import *
from ...backend.home.models import Config
from ...backend.resume.models import *


# Create your views here.

class HomeView(ListView):
    model = Config
    template_name = "frontend/home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['skills'] = Skill.objects.filter(status=True).order_by('position')
        context['activeUrl'] = about

        return context


class ResumeView(ListView):
    model = Config
    template_name = "frontend/resume/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['educations'] = Education.objects.filter(status=True).order_by('position')
        context['keySkills'] = KeySkill.objects.filter(status=True).order_by('position')
        context['experiences'] = Experience.objects.filter(status=True).order_by('position')
        context['activeUrl'] = profile

        return context


class WorksView(ListView):
    model = Config
    template_name = "frontend/works/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['activeUrl'] = works

        return context


class BlogView(ListView):
    model = Config
    template_name = "frontend/blogs/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['activeUrl'] = blogs

        return context


class ContactView(ListView):
    model = Config
    template_name = "frontend/contact/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['activeUrl'] = contact

        return context
