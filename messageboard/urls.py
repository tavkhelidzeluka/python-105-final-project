from django.contrib import admin
from django.urls import path, include

from messageboard.views import Message_view, about_view, home_view

app_name = "messageboard"

urlpatterns = [
    path("", home_view, name="home"),
    path("home/", home_view),
    path("about/", about_view, name="about"),
    path("message/", Message_view.as_view(), name="message")
]