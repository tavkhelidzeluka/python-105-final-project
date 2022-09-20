from django.contrib import admin
from django.urls import path, include

from board.views import PostView, about_view, home_view

app_name = "messageboard"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("posts/", PostView.as_view(), name="posts")
]