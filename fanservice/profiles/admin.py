from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from profiles.forms import UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    add_form = UserCreationForm

# from .models import Profile
#
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     """Профиль пользователя"""
#     list_display = ("user", "first_name", "last_name", "phone", "email_two")
    
