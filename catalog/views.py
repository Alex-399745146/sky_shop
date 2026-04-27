# catalog/views.py
"""
1. Контроллеры (начинаем с контроллеров) для простоты с начало
можем простой контроллер написать
def index(request):
    return HttpResponse("Страница приложения women.")
"""
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")
