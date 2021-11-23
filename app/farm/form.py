from django import forms
from django.forms import ModelForm
from .models import Farm


class FarmDetailsForm(ModelForm):
    class Meta:
        model = Farm
        fields = ['id', 'name', 'description', 'phone_no', 'location_state', 'city']
        widgets = {
            'city': forms.HiddenInput(),
            'location_state': forms.HiddenInput(),
        }


