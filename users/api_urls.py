
from django import template
from django.urls import path
from .api_views import ResetPasswordConfirmView, login, ForgetPasswordView


urlpatterns = [
 path("login",login, name="login_api"),
 path("reset_password",ForgetPasswordView.as_view(), name="reset_password_api"),
 path("reset_password/confirm",ResetPasswordConfirmView.as_view(), name="reset_password_confirm_api"),
]