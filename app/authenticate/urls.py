from django.urls import path
from . import views
from .forms import UserLogin
from django.contrib.auth.views import LogoutView

app_name='authenticate'
urlpatterns = [
  path('', views.user_register, name='user_register'),
  path('login/', UserLogin.as_view(), name='user_login'),
  path('logout', LogoutView.as_view(), name='user_logout')
]
