from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from apps.backend.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='UserName')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            # if not user:
            # raise forms.ValidationError('User not found')
            return super(LoginForm, self).clean()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'image',
            'is_active'
        ]
