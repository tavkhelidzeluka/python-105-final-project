from django.contrib import admin
from django.urls import path, include
from .views import SignUp
from django.contrib.auth.views import LoginView, LogoutView

app_name = "account"

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]