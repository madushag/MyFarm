from django import forms
from django.forms import ModelForm

from .models import Produce


class ProduceDetailsForm(ModelForm):
    class Meta:
        model = Produce
        fields = ['name', 'description', 'price', 'min_quantity', 'is_organic']

    # name = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of farm'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description of farm'}))
    # phone_no = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone number of farm as 123-456-7890'}))


