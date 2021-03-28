from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import RegisterView , VerifyEmailView
from dj_rest_auth.views import LogoutView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import path, re_path
from rest_auth.views import LoginView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', obtain_auth_token, name='login-token'),
    # path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',  PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]

# path('old-login/', LoginView.as_view()),
#