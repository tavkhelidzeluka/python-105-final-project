from django.contrib.auth.mixins import LoginRequiredMixin
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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = "post_create.html"
    fields = ["title", "text"]
    login_url = "account:login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Posts
    template_name = "post_detail.html"
    fields = ["title", "text"]
    login_url = "account:login"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = "post_detail.html"
    success_url = reverse_lazy("postsite:posts")
    login_url = "account:login"
