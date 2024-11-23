from django.forms import ModelForm
from .models import *


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = [
            'label',
            'url',
            'icon',
            'status',
        ]
