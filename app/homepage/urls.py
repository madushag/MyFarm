from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
  path('', views.homepage, name='home'),
  path('<str:name>/list_farm_produce', views.list_farm_produce, name='list_farm_produce'),
]
