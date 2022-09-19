from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404

# Create your views here.

def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

