from django.urls import path, include
from . import views

app_name = 'items'

urlpatterns = [
    path('add_item_page', views.Add_Item_page, name='add_item'),
    path('add_item_completed', views.Add_Item_Completed, name='add_item_completed'),
]