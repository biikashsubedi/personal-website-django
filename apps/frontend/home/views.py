import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from personalPortfoloi.metaData import *
from ...backend.contact.models import ContactUs
from ...backend.home.models import Config
from ...backend.resume.models import *


# Create your views here.
# @method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')
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


import os
import email
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


def preview_page(request):
    return render(request, 'frontend/file/index1.html')


import os
import email
import base64
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

#
# @xframe_options_exempt
# def preview_mhtml(request):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'file', 'Discussion 1.mhtml')
#
#     with open(file_path, 'rb') as f:
#         msg = email.message_from_binary_file(f)
#
#     html_parts = []
#     cid_map = {}
#
#     for part in msg.walk():
#         content_type = part.get_content_type()
#         content_id = part.get("Content-ID")
#
#         if content_type == "text/html":
#             html_parts.append(part.get_payload(decode=True).decode(errors="ignore"))
#
#         elif content_id:
#             cid = content_id.strip("<>")
#             data = part.get_payload(decode=True)
#             encoded = base64.b64encode(data).decode()
#             cid_map[cid] = f"data:{content_type};base64,{encoded}"
#
#     if not html_parts:
#         return HttpResponse("No HTML found.")
#
#     # 🔥 IMPORTANT: choose the LARGEST html part (real page)
#     html_content = max(html_parts, key=len)
#
#     # Replace CID images
#     for cid, data_url in cid_map.items():
#         html_content = html_content.replace(f"cid:{cid}", data_url)
#
#     return HttpResponse(html_content, content_type="text/html")


import os
from django.conf import settings
from django.http import FileResponse


from django.http import FileResponse
import os
from django.conf import settings

def preview_mhtml(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'file', 'Discussion 1.mhtml')
    return FileResponse(
        open(file_path, 'rb'),
        content_type='multipart/related'
    )