from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from messageboard.models import Messages
from django.views.generic import ListView

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

class Message_view(ListView):
    model = Messages
    template_name = "message.html"