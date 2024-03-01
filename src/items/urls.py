from django.urls import include, path

from . import views

app_name = 'items'

urlpatterns = [
    path('add_item_page/', views.Add_Item_page, name='add_item'),
    path('add_item_completed/', views.Add_Item_Completed, name='add_item_completed'),
    path('item_details/<int:item_id>/', views.Item_Detail, name='item_details'),
    path('item_details/<int:item_id>/like/', views.LikeItem.as_view(), name='like'),    
]