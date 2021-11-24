from django.urls import path
from . import views
# from homepage import views as homepage_views


app_name = 'produce'
urlpatterns = [
    path('<int:farm_id>/list', views.list_produce, name='list'),
    path('<int:farm_id>/customer', views.customer, name='customer'),
    path('<int:farm_id>/add', views.add, name='add'),
    path('add', views.add, name='add'),
    path('<int:produce_id>/edit', views.edit, name='edit'),
    path('<int:produce_id>/delete', views.delete, name='delete'),
]
