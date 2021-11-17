from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': "form-control"}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': "form-control"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': "form-control"}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Input a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': "form-control"}))
    password1 = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control"}))
    password2 = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.PasswordInput(attrs={'placeholder': 'Password (again)', 'class': "form-control"}))
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserLogin(LoginView):
    template_name = 'authenticate/login.html'
