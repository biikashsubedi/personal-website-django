import json

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from .forms import LinkForm
from .models import *
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy

from ..profiles.models import Profile
from ..resume.models import Skill, Education, Experience


# Create your views here.

class HomeView(ListView):
    model = Config
    template_name = "backend/home/index.html"


def ExtractData(request):
    try:
        with open('personalPortfoloi/data.json', 'r') as file:
            data = json.load(file)
            Profile.objects.all().delete()
            Education.objects.all().delete()
            Experience.objects.all().delete()
            Link.objects.all().delete()
            Skill.objects.all().delete()

            checkExists = Profile.objects.filter(name=data['name']).exists()
            if not checkExists:
                checkExists = Profile(
                    name=data['name'],
                    job_title=data['job_title'],
                    phone1=data['phone1'],
                    email1=data['email1'],
                    location=data['location'],
                    introduction=data['introduction'],
                    website=data['website'],
                    facebook_link=data['facebook_link'],
                    linkedin_link=data['linkedin_link'],
                    instagram_link=data['instagram_link'],
                    twitter_link=data['twitter_link'],
                    gmap_link=data['gmap_link'],
                )
                checkExists.save()

            for index, value in data['skills'].items():
                checkExists = Skill.objects.filter(label=index).exists()
                if not checkExists:
                    icon = value.get('icon', '')
                    background = value.get('background')

                    checkExists = Skill(
                        label=index,
                        value=value['description'],
                        icon=icon,
                        background=background
                    )
                    checkExists.save()

            for index, value in data['educations'].items():
                checkExists = Education.objects.filter(label=index).exists()
                if not checkExists:
                    checkExists = Education(
                        label=index,
                        year=value['year'],
                        location=value['location'],
                        background=value['background'],
                        value=value['value'],
                    )
                    checkExists.save()

            for index, value in data['experiences'].items():
                checkExists = Experience.objects.filter(label=index).exists()
                if not checkExists:
                    checkExists = Experience(
                        label=index,
                        type='text',
                        year=value,
                        location=value,
                        value=value
                    )
                    checkExists.save()

            for index, value in data['links'].items():
                checkExists = Link.objects.filter(label__iexact=index).exists()
                if not checkExists:
                    checkExists = Link(
                        label=index,
                        url=value['url'],
                        icon=value['icon']
                    )
                    checkExists.save()

            messages.success(request, 'Successfully data reset.')
            return redirect(reverse('profile:index'))


    except Exception as e:
        print('=============================================================================================================')
        print(f"str{e}")
        print('=============================================================================================================')
        messages.success(request, 'Unable to set default data.')
        return redirect(reverse('profile:index'))


class LinkIndex(ListView):
    model = Link
    template_name = "backend/link/index.html"


class LinkCreate(SuccessMessageMixin, CreateView):
    model = Link
    template_name = "backend/link/form.html"
    form_class = LinkForm
    success_message = "Link Created Successfully."
    success_url = reverse_lazy('home:link.index')


class LinkUpdate(SuccessMessageMixin, UpdateView):
    model = Link
    template_name = "backend/link/form.html"
    form_class = LinkForm
    success_message = "Link Updated Successfully."
    success_url = reverse_lazy('home:link.index')


class LinkDelete(SuccessMessageMixin, DeleteView):
    model = Link
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Link Deleted Successfully."
    success_url = reverse_lazy('home:link.index')
