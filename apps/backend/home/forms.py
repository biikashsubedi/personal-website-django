from django import forms
from django.forms import ModelForm
from .models import *


class LinkForm(ModelForm):
    url = forms.CharField(label='Url',
                          widget=forms.Select(choices=URLS, attrs={'class': "form-control"}))

    class Meta:
        model = Link
        fields = [
            'label',
            'url',
            'icon',
            'status',
        ]
