from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *


class Index(ListView):
    model = Education
    template_name = "backend/resume/education/index.html"


class Create(SuccessMessageMixin, CreateView):
    model = Education
    template_name = "backend/resume/education/form.html"
    form_class = EducationForm
    success_message = "Education Created Successfully."
    success_url = reverse_lazy('resume:education.index')


class Update(SuccessMessageMixin, UpdateView):
    model = Education
    template_name = "backend/resume/education/form.html"
    form_class = EducationForm
    success_message = "Education Updated Successfully."
    success_url = reverse_lazy('resume:education.index')


class Delete(SuccessMessageMixin, DeleteView):
    model = Education
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Education Deleted Successfully."
    success_url = reverse_lazy('resume:education.index')


class ExperienceIndex(ListView):
    model = Experience
    template_name = "backend/resume/experience/index.html"


class ExperienceCreate(SuccessMessageMixin, CreateView):
    model = Experience
    template_name = "backend/resume/experience/form.html"
    form_class = ExperienceForm
    success_message = "Experience Created Successfully."
    success_url = reverse_lazy('resume:experience.index')


class ExperienceUpdate(SuccessMessageMixin, UpdateView):
    model = Experience
    template_name = "backend/resume/experience/form.html"
    form_class = ExperienceForm
    success_message = "Experience Updated Successfully."
    success_url = reverse_lazy('resume:experience.index')


class ExperienceDelete(SuccessMessageMixin, DeleteView):
    model = Experience
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Experience Deleted Successfully."
    success_url = reverse_lazy('resume:experience.index')

class SkillIndex(ListView):
    model = Skill
    template_name = "backend/resume/skill/index.html"


class SkillCreate(SuccessMessageMixin, CreateView):
    model = Skill
    template_name = "backend/resume/skill/form.html"
    form_class = SkillForm
    success_message = "Skill Created Successfully."
    success_url = reverse_lazy('resume:skill.index')


class SkillUpdate(SuccessMessageMixin, UpdateView):
    model = Skill
    template_name = "backend/resume/skill/form.html"
    form_class = SkillForm
    success_message = "Skill Updated Successfully."
    success_url = reverse_lazy('resume:skill.index')


class SkillDelete(SuccessMessageMixin, DeleteView):
    model = Skill
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Skill Deleted Successfully."
    success_url = reverse_lazy('resume:skill.index')
