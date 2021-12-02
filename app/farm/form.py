from django import forms
from django.forms import ModelForm
from .models import Farm


class FarmDetailsForm(ModelForm):
    class Meta:
        model = Farm
        fields = ['id', 'name', 'description', 'phone_no', 'location_state', 'city', 'website_url', 'location_lng', 'location_lat', 'location_name', 'location_url', 'location_address']
        widgets = {
            'city': forms.HiddenInput(),
            'location_state': forms.HiddenInput(),
            'location_lat': forms.HiddenInput(),
            'location_lng': forms.HiddenInput(),
            'location_name': forms.HiddenInput(),
            'location_url': forms.HiddenInput(),
            'location_address': forms.HiddenInput(),
        }


