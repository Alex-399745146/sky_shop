# blog/admin.py

from django.contrib import admin
from .models import BlogPost


# Регистрация модели BlogPost в административной панели.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Настройка административной панели для модели BlogPost."""

    # Поля, отображаемые в списке записей.
    list_display = (
        "id",
        "title",
        "created_at",
        "is_published",
        "views_count",
    )

    # Фильтры в боковой панели для быстрого поиска.
    list_filter = (
        "is_published",
        "created_at",
        "title",
    )

    # Поля, по которым выполняется поиск в админке.
    search_fields = ("title", "content")

    # Автозаполнение slug на основе title (если поле slug существует).
    prepopulated_fields = {"slug": ("title",)} if hasattr(BlogPost, "slug") else {}
