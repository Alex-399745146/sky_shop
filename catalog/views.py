# catalog/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, FormView

from blog.models import BlogPost
from catalog.models import Product
from catalog.forms import ContactForm, ProductForm


# Create - создание продукта.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """Редирект на страницу созданного продукта."""
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


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
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """Редирект на страницу отредактированного продукта."""
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


# Delete - удаление продукта.
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactFormView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contacts')

    def form_valid(self, form):
        # Получаем данные из формы
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        # Здесь можно отправить email, сохранить в БД и т.д.
        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")

        return super().form_valid(form)
