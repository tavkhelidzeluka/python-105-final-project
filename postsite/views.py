from turtle import title
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from postsite.models import Posts
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

class PostView(ListView):
    model = Posts
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Posts
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Posts
    template_name = "post_create.html"
    fields = "__all__"

class PostUpdateView(UpdateView):
    model = Posts
    template_name = "post_detail.html"
    fields = ["title", "text"]

class PostDeleteView(DeleteView):
    model = Posts
    template_name = "post_detail.html"
    success_url = reverse_lazy
