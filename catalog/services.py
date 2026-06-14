# catalog/services.py
from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_products_by_category(category_id: int):
    """
    Возвращает список продуктов в указанной категории.
    При включённом CACHE_ENABLED сначала читаем из кэша (Redis),
    иначе — из БД и кладём в кэш.
    """
    cache_key = f"category_products:{category_id}"

    if getattr(settings, "CACHE_ENABLED", False):
        products = cache.get(cache_key)
        if products is not None:
            return products

    products = Product.objects.filter(
        category_id=category_id,
        is_published=True,
    )

    if getattr(settings, "CACHE_ENABLED", False):
        cache.set(cache_key, products, 60 * 5)  # 5 минут.

    return products


def get_product_list_from_cache():
    """
    Возвращает список (QuerySet) всех опубликованных продуктов.
    При включённом CACHE_ENABLED сначала пытается взять из кэша.
    """
    cache_key = "product_list_all"

    # 1. Пробуем из кэша.
    if getattr(settings, "CACHE_ENABLED", False):
        products = cache.get(cache_key)
        if products is not None:
            return products

    # 2. Если в кэше нет — идём в БД.
    products = Product.objects.filter(is_published=True)

    # 3. Кладём результат в кэш на 5 минут.
    if getattr(settings, "CACHE_ENABLED", False):
        cache.set(cache_key, products, 60 * 5)

    return products
