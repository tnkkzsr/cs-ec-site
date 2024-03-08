from django.urls import path, include
from . import views

app_name = 'settlement'

urlpatterns = [
    path('confirm/<int:item_id>', views.confirm, name='confirm'),
    path('completed/', views.completed, name='completed'),
    path('AddAddress/<int:user_id>', views.AddAddress.as_view(), name='AddAddress'),
    path('stripe', views.stripe, name='stripe')
]