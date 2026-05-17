# catalog/urls.py
"""
Формируем маршруты и создаем пространство имён в главном URLS.PY
"""

from django.urls import path

from . import views

# Задаем пространство имен в файле маршрутизации приложения.
app_name = "catalog"

urlpatterns = [
    path("", views.catalog_list, name="catalog_list"),    # 127.0.0.1:8000/
    # path("", views.home, name="home"),                       # 127.0.0.1:8000/
    path("home/", views.home, name="home_alt"),          # 127.0.0.1:8000/home/
    path("contacts/", views.contacts, name="contacts"),  # 127.0.0.1:8000/contacts/
    path("contact/", views.contact, name="contact"),     # 127.0.0.1:8000/contact/
]
