from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Shift


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            'name',
            'phone_number',
            'workspace',
            'date',
            'checkin_time',
            'checkout_time',
            'shift_type',
            'hourly_rate',
        ]
        widgets = {
            'date': forms.TimeInput(attrs={'type': 'date', 'class': 'form-control'}),
            'checkin_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'checkout_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-select form-control'}),
            'workspace': forms.Select(attrs={'class': 'form-select form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Update: show existing checkin and checkout times
            self.fields['checkout_time'].initial = timezone.localtime().strftime('%H:%M')
            self.fields['date'].initial = self.instance.date.strftime('%Y-%m-%d')
            if self.instance.checkin_time:
                self.fields['checkin_time'].initial = self.instance.checkin_time

            if self.instance.checkout_time:
                self.fields['checkout_time'].initial = self.instance.checkout_time
        else:
            # Create: default checkin_time to current time, leave checkout_time blank
            self.fields['date'].initial = timezone.localtime().today().strftime('%Y-%m-%d')
            self.fields['checkin_time'].initial = timezone.localtime().strftime('%H:%M')
            self.fields['checkout_time'].initial = ''

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        checkin_time = cleaned_data.get("checkin_time")
        checkout_time = cleaned_data.get("checkout_time")
        workspace = cleaned_data.get("workspace")

        # Rule 1: checkout must be after checkin
        if checkin_time and checkout_time:
            if checkout_time <= checkin_time:
                self.add_error("checkout_time", "Checkout time must be greater than checkin time.")

        # Rule 2: only one insert per day per workspace
        if not self.instance.pk and workspace and checkin_time:
            today = timezone.localdate()
            existing_shift = Shift.objects.filter(
                workspace=workspace,
                date=date
            ).exists()
            if existing_shift:
                raise ValidationError(
                    "You can only create one shift per workspace per day.")

        return cleaned_data
