from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
#
def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            request.session['username'] = username
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'homepage/homepage.html')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/authenticate.html', {'form': form})
