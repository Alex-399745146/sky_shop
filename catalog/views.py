# catalog/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from blog.models import BlogPost
from catalog.forms import ContactForm, ProductForm
from catalog.models import Product


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_post"] = BlogPost.objects.filter(is_published=True).order_by("-created_at").first()
        return context


# Read - детально продукт.
class ProductDetailView(DetailView):
    model = Product


# Update - редактирование продукта.
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    # Куда перенаправлять неавторизованных.
    login_url = "users:login"

    def get_success_url(self):
        """Редирект на страницу отредактированного продукта."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


# Delete - удаление продукта.
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    # Куда перенаправлять неавторизованных.
    login_url = "users:login"


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
