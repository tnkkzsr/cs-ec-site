from django.urls import path, include
from . import views

app_name = 'items'

urlpatterns = [
    path('add_item', views.Additem, name='add_item'),
]