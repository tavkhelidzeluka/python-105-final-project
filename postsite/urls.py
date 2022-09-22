from django.contrib import admin
from django.urls import path, include
from .views import home_view, about_view, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "postsite"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    #path("posts/", PostView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/new", PostCreateView.as_view(), name="post_new"),
    path("posts/edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
]