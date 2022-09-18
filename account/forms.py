from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class AddUserProfile(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields

class EditUserProfile(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = UserChangeForm.Meta.fields