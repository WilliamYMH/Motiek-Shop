from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

from . import views

urlpatterns = [
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/done/',
         PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
