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


class ExperienceForm(ModelForm):
    value = forms.CharField(label='value',
                            widget=forms.Textarea(attrs={'class': "form-control", 'rows': "4"}))
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
