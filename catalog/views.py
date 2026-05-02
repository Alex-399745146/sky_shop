# catalog/views.py
"""
1. Контроллеры (начинаем с контроллеров) для простоты с начало
можем простой контроллер написать
def index(request):
    return HttpResponse("Страница приложения women.")
"""

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name} ваш номер:{phone} и сообщение:{message} отправлены!")
    return render(request, "catalog/contacts.html")
