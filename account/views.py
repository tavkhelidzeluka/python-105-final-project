from tkinter.tix import Form
from django.shortcuts import render
from .models import UserProfile
from .forms import AddUserProfile
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    form_class = AddUserProfile
    template_engine = "signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form: _ModelFormT) -> HttpResponse:
        return super().form_valid(form)


