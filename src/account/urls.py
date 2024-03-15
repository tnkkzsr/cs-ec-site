from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

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
    path('reset_password/', views.PasswordReset.as_view(), name='reset_password'),
    path('password_reset_sent', views.PasswordResetSent.as_view(), name='password_reset_sent'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('delete/<int:pk>', views.UserDeleteView.as_view(), name='delete'),
    path('delete_done/', views.UserDeleteDoneView.as_view(), name='delete_done'),
    path('favorite_items/', views.FavoriteItems, name='favorite_items')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)