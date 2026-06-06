# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Админка для нашей кастомной модели пользователя."""

    # Какие поля показывать в списке пользователей
    list_display = ("email", "phone", "country", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "country")

    # Группировка полей на странице редактирования пользователя
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name", "avatar", "phone", "country")}),
        ("Права доступа", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    # Поля, которые будут доступны при создании пользователя через админку
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_superuser", "is_active"),
            },
        ),
    )

    search_fields = ("email", "phone", "first_name", "last_name")
    ordering = ("email",)
