from django.contrib import admin
from django.urls import path, include

from messageboard.views import homepage

app_name = "messageboard"

urlpatterns = [
    path("", homepage, name="home"),
    path("home/", homepage, name="home"),
]