from django.contrib import admin
from django.urls import path, include
from .views import home_view, about_view, PostView, PostDetailView

app_name = "postsite"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    #path("posts/", PostView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    #path("posts/delete/<int:pk>/",)
]