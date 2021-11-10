from django import forms


class FarmDetails(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(label='Description')
    phone_no = forms.CharField(label='Phone No.', max_length=12)
