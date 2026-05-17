# catalog/views.py
"""
1. Контроллеры (начинаем с контроллеров) для простоты с начало
можем простой контроллер написать
def index(request):
    return HttpResponse("Страница приложения women.")
"""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def catalog_list(request):
    """Вывод всех карточек продукта."""
    products = Product.objects.all()  # Все карточки товаров.
    context = {"products": products}  # Контекстный словарь для передачи данных в шаблон.
    return render(request, "products_list.html", context)


def catalog_detail(request, pk):
    """Детальная страница товара."""
    # get_object_or_404 безопаснее и правильнее, чем .get().
    product = get_object_or_404(Product, id=pk)  # Запрос в БД.
    context = {"product": product}
    return render(request, "product_detail.html", context)


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
