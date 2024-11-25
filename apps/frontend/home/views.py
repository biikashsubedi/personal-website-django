from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from personalPortfoloi.metaData import *
from ...backend.contact.models import ContactUs
from ...backend.home.models import Config
from ...backend.resume.models import *


# Create your views here.
@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
class HomeView(ListView):
    model = Config
    template_name = "frontend/home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['skills'] = Skill.objects.filter(status=True).order_by('position')
        context['activeUrl'] = about

        return context


@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
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


@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
class WorksView(ListView):
    model = Config
    template_name = "frontend/works/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['works'] = Project.objects.filter(status=True).order_by('position')
        context['activeUrl'] = works

        return context


@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
class BlogView(ListView):
    model = Config
    template_name = "frontend/blogs/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['activeUrl'] = blogs

        return context


@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
class ContactView(ListView):
    model = Config
    template_name = "frontend/contact/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = {}
        context['activeUrl'] = contact

        return context


@require_POST
# @ratelimit(key='ip', rate='1/h')
def store_contact_us(request):
    if getattr(request, 'limited', False):
        return JsonResponse({'status': False, 'message': 'More requests detected, please try again.'}, status=429)

    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name, email=email, phone=phone, message=message)

        return JsonResponse({'status': True, 'message': 'Thanks for contacting us. We will reach you soon!'})
    except Exception as e:
        return JsonResponse({'status': False}, status=400)
