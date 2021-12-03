from django import forms
from django.forms import ModelForm
from .models import Produce


class ProduceForm(ModelForm):
    class Meta:
        model = Produce
        fields = ['id', 'name', 'description', 'price', 'min_quantity', 'is_organic', 'farm', 'mode_of_sale']
        widgets = {
            'id': forms.HiddenInput(),
            'farm': forms.TextInput(attrs={'style': 'display:none'}),
            # 'picture': forms.FileInput(),
        }




