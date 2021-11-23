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


    # id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of farm'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description of farm'}))
    # phone_no = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control',  'oninvalid':"this.setCustomValidity('Enter a valid phone number using format 123-456-7890')", 'oninput':"this.setCustomValidity('')", 'pattern':'[0-9]{3}-[0-9]{3}-[0-9]{4}', 'placeholder':'Phone number of farm as 123-456-7890'}))
    # location_state = forms.ModelChoiceField(attrs={'class': 'form-control'})


