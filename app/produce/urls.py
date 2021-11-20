from django.urls import path
from . import views
from homepage import views as homepage_views


app_name = 'produce'
urlpatterns = [
    path('<int:farm_id>/list', views.index, name='index'),
    # path('<int:farm_id>/customer', views.customer, name='customer'),
    # path('/', homepage_views.homepage, name='homepage'),
    path('add', views.add, name='add'),
    # path('<int:farm_id>/details', views.details, name='details'),
    # path('<int:farm_id>/delete', views.delete, name='delete'),
]
