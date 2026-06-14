# catalog/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from blog.models import BlogPost
from catalog.forms import ContactForm, ProductForm
from catalog.models import Product
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create - создание продукта.
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # Куда перенаправлять неавторизованных.
    login_url = "users:login"

    def form_valid(self, form):
        """
        Перед сохранением формы привязываем товар к текущему пользователю.
        Поле owner в форме не показываем — оно заполняется автоматически.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Редирект на страницу созданного продукта."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


# Read - весь список.
class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_post"] = BlogPost.objects.filter(is_published=True).order_by("-created_at").first()
        return context


# Read - детально продукт.
@method_decorator(cache_page(60 * 5), name="dispatch")  # 5 минут жизнь кэша.
class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


# Update - редактирование продукта.
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # Куда перенаправлять неавторизованных.
    login_url = "users:login"
    # permission_required = "catalog.change_product"

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def handle_no_permission(self):
        # Если пользователь залогинен, но не владелец — 403 error.
        if self.request.user.is_authenticated:
            raise PermissionDenied("Вы не можете редактировать этот продукт")
        # Если не залогинен — стандартное поведение LoginRequiredMixin.
        return super().handle_no_permission()

    def get_success_url(self):
        """Редирект на страницу отредактированного продукта."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


# Delete - удаление продукта.
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Модель, с которой работает представление — Product.
    model = Product
    # После успешного удаления перенаправляем на список продуктов.
    success_url = reverse_lazy("catalog:product_list")
    # Куда перенаправлять неавторизованных.
    login_url = "users:login"
    # Удаление только по праву.
    # permission_required = "catalog.delete_product"

    def test_func(self):
        """
        Проверка прав доступа:
        - удалять может владелец товара;
        - или пользователь из группы "Модераторы".
        """
        product = self.get_object()  # Текущий продукт из БД.
        user = self.request.user  # Текущий пользователь.

        is_owner = product.owner == user  # Является ли он владельцем.
        is_moderator = user.groups.filter(name="Модераторы").exists()  # Состоит ли в группе модераторов.

        # Доступ есть, если пользователь — владелец или модератор.
        return is_owner or is_moderator

    def handle_no_permission(self):
        """
        Поведение при отсутствии прав:
        - если пользователь залогинен, но не имеет доступа — 403 с сообщением;
        - если не залогинен — сработает стандартная логика LoginRequiredMixin.
        """
        if self.request.user.is_authenticated:
            raise PermissionDenied("Вы не можете удалить этот продукт")
        return super().handle_no_permission()


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("catalog:contacts")

    def form_valid(self, form):
        # Получаем данные из формы.
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]
        # Здесь можно отправить email, сохранить в БД и т.д.
        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")
        return super().form_valid(form)


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"
    login_url = "users:login"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect("catalog:product_detail", pk=product.pk)
