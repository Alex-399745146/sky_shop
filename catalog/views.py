# catalog/views.py

from django.views.generic import DetailView, ListView, TemplateView

from blog.models import BlogPost
from catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем последнюю опубликованную статью
        context["latest_post"] = BlogPost.objects.filter(is_published=True).order_by("-created_at").first()
        return context


class ProductDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {message}")

        context = self.get_context_data(success=True, name=name, phone=phone, message=message)
        return self.render_to_response(context)
