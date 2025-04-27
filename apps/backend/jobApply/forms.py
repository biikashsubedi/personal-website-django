from django.forms import ModelForm
from .models import *


class ContactUsForm(ModelForm):
    class Meta:
        model = jobApply
        fields = [
            'name',
            'email',
            'message'
        ]
