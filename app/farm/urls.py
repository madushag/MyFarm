from django.urls import path
from . import views


app_name = 'farm'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:farm_id>/', views.details, name='details'),
    path('add', views.add, name='add'),
    path('<int:farm_id>/update', views.update, name='update'),
]
