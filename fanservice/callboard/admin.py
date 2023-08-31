from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Advert, UserResponse


# @admin.register(Category)
# class CategoryAdmin(MPTTModelAdmin):
#     """Категории"""
#     list_display = ("name", "parent", "id")
#     mptt_level_indent = 20
#     prepopulated_fields = {"slug": ("name",)}


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        "user",
        "category",
        "created",
    )
    list_display_links = ("subject",)
    list_filter = ("user", "category")
@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    """Отклики"""
    list_display = (
        "id",
        "user",
        "advert",
        "subject",
    )
    list_display_links = ("subject",)
    list_filter = ("user",)