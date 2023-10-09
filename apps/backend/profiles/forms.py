from django import forms
from django.forms import ModelForm
from .models import Profile
from ckeditor.widgets import CKEditorWidget


class ProfileForm(ModelForm):
    introduction = forms.CharField(widget=CKEditorWidget(attrs={'class': "form-control"}))

    class Meta:
        model = Profile
        fields = [
            'name',
            'introduction',
            'image',
            'resume',
            'phone1',
            'phone2',
            'completed_project',
            'company_linked',
            'love',
            'email1',
            'email2',
            'website',
            'facebook_link',
            'linkedin_link',
            'instagram_link',
            'twitter_link',
            'tor_link',
            'gmap_link',
            'status',
        ]
