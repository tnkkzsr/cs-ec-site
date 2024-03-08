from django.urls import include, path

from . import views

app_name = 'settlement'

urlpatterns = [
    path('AddressSelect/<int:item_id>', views.confirm, name='AddressSelect'),
    path('completed/', views.completed, name='completed'),
    path('AddAddress/<int:user_id>', views.AddAddress.as_view(), name='AddAddress'),
    path('stripe', views.stripe, name='stripe'),
    path('payment/', views.PayView.as_view(), name='payment')
]