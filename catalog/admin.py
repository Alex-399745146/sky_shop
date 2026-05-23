"""
Административная панель для приложения catalog.
Регистрация моделей Category и Product с настройками отображения.
"""

from django.contrib import admin

from catalog.models import Category, Product


#  Регистрационная модель для Category.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка категорий."""

    # Отображение в списке.
    list_display = (
        "id",
        "name"
    )


#  Регистрационная модель для Product.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка продуктов."""

    list_display = ("id", "name", "price", "category")  # Отображение в списке.
    list_filter = ("category",)  # Фильтр продукции по категории.
    search_fields = ("name", "details")  # Поиск по имени и описанию.
