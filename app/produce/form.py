from django import forms
from django.forms import ModelForm
from django.http import request

from .models import Produce
# from farm.models import Farm


class ProduceForm(ModelForm):
    class Meta:
        model = Produce
        fields = ['id', 'name', 'description', 'price', 'min_quantity', 'is_organic', 'farm']
        widgets = {
            'id': forms.HiddenInput(),
            'farm': forms.Select(attrs={'style': 'display:none'}),
        }

    # def __init__(self, user, *args, **kwargs):
    #     super(ProduceForm, self).__init__(*args, **kwargs)  # populates the post
    #     # id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    #     # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of produce'}))
    #     # price = forms.FloatField()
    #     # min_quantity = forms.FloatField()
    #     # is_organic = forms.BooleanField(required=False)
    #     # farm = forms.ModelChoiceField(queryset=Farm.objects.all())
    #     self.fields['farm'].queryset = Farm.objects.filter(farmer=user)  # only show farms that belong to the user

    # is_organic = forms.BooleanField(required=False)




