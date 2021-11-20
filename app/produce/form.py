from django import forms
from django.forms import ModelForm

from .models import Produce


class ProduceDetailsForm(ModelForm):
    class Meta:
        model = Produce
        fields = ['name', 'description', 'price', 'min_quantity', 'is_organic', 'farm']

    farm_name = forms.CharField(widget=forms.HiddenInput())

