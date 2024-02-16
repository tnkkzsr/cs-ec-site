from django.urls import path, include
from . import views

app_name = 'top'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('account/', views.AccountView.as_view(), name='account')
]