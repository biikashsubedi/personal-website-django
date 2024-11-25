from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm
from .models import *


class EducationForm(ModelForm):
    value = forms.CharField(label='value',
                            widget=forms.Textarea(attrs={'class': "form-control", 'rows': "4"}))

    class Meta:
        model = Education
        fields = [
            'label',
            'year',
            'location',
            'background',
            'value',
            'status',
            'position',
        ]


class SkillForm(ModelForm):
    value = forms.CharField(label='value',
                            widget=forms.Textarea(attrs={'class': "form-control", 'rows': "4"}))
    class Meta:
        model = Skill
        fields = [
            'label',
            'value',
            'icon',
            'background',
            'status',
            'position',
        ]


class KeySkillForm(ModelForm):
    class Meta:
        model = KeySkill
        fields = [
            'label',
            'status',
            'position',
        ]


class ExperienceForm(ModelForm):
    value = forms.CharField(widget=CKEditorWidget(attrs={'class': "form-control"}))
    class Meta:
        model = Experience
        fields = [
            'label',
            'type',
            'year',
            'location',
            'value',
            'status',
            'position',
        ]


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'label',
            'url',
            'icon',
            'background',
            'status',
            'position',
        ]
