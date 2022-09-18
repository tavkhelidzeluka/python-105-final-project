from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import AddUserProfile, EditUserProfile

# Register your models here.

class AdminProfile(UserAdmin):
    add_form = AddUserProfile
    form = EditUserProfile
    model = UserProfile

admin.site.register(UserProfile, AdminProfile)