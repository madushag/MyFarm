from django.urls import path
from . import views


app_name = 'farm'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:farm_id>/details', views.details, name='details'),
    path('<int:farm_id>/delete', views.delete, name='delete'),
]
