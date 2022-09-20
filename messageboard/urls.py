from django.contrib import admin
from django.urls import path, include

from messageboard.views import aboutpage, homepage

app_name = "messageboard"

urlpatterns = [
    path("", homepage, name="home"),
    path("home/", homepage),
    path("about/", aboutpage, name="about"),
]