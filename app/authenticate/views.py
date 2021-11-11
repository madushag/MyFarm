from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from homepage.views import homepage


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
            return redirect('homepage:home')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/authenticate.html', {'form': form})



def login_view(request):
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    
    # Check if authentication is successful
    if user is not None:
      login(request, user)
      return render(request, 'authenticate/authenticate.html')
    else:
      return render(request, 'authenticate/login.html', {
        'message': 'Invalid username and/or password.'
      })

  return render(request, 'authenticate/login.html')

  