from django import forms
from django.forms import ModelForm

from .models import Produce, Farm


class ProduceForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of produce'}))
    price = forms.FloatField()
    min_quantity = forms.FloatField()
    is_organic = forms.BooleanField(required=False)
    farm = forms.ModelChoiceField(queryset=Farm.objects.all())


    class Meta:
        model = Produce
        fields = ['id','name', 'price', 'min_quantity', 'is_organic', 'farm']
