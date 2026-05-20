# catalog/urls.py
"""
Формируем маршруты и создаем пространство имён в главном URLS.PY
"""

from django.urls import path

from . import views

from .views import ProductListView, ProductDetailView, ContactTemplateView



# Задаем пространство имен в файле маршрутизации приложения.
app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    # path("", views.catalog_list, name="catalog_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="catalog_detail"),
    # path("product/<int:pk>/", views.catalog_detail, name="catalog_detail"),
    path("contacts/", ContactTemplateView.as_view(), name="contact"),
    # path("contacts/", views.contact, name="contact"),
]
