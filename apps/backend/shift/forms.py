from django.forms import ModelForm
from .models import *


class ContactUsForm(ModelForm):
    class Meta:
        model = Shift
        fields = [
            'name',
            'email',
            'message'
        ]
