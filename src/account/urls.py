from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.AccountView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('signup_done/', views.SignupDone.as_view(), name='signup_done'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done')
]