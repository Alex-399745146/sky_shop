# catalog/views.py
"""
1. Контроллеры (начинаем с контроллеров) для простоты с начало
можем простой контроллер написать
def index(request):
    return HttpResponse("Страница приложения women.")
"""

from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


# def catalog_list(request):
#     """Вывод всех карточек продукта."""
#     products = Product.objects.all()  # Все карточки товаров.
#     context = {"products": products}  # Контекстный словарь для передачи данных в шаблон.
#     return render(request, "catalog/product_list.html", context)


class ProductDetailView(DetailView):
    model = Product


# def catalog_detail(request, pk):
#     """Детальная страница товара."""
#     # get_object_or_404 безопаснее и правильнее, чем .get().
#     product = get_object_or_404(Product, id=pk)  # Запрос в БД.
#     context = {"product": product}
#     return render(request, "catalog/product_detail.html", context)


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")

        context = self.get_context_data(
            success=True,
            name=name,
            phone=phone,
            message=message
        )
        return self.render_to_response(context)


# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         return HttpResponse(f"Спасибо, {name} ваш номер:{phone} и сообщение:{message} отправлены!")
#     return render(request, "catalog/contacts.html")
