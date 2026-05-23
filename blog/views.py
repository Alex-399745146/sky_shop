# blog/views.py

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import BlogPost


# Read - весь список.
class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        # Показываем только опубликованные статьи.
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")


# Read - детально статью.
class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        # Получаем объект для увеличения его числа.
        obj = super().get_object(queryset)
        # Увеличиваем число просмотров статьи.
        obj.views_count += 1
        obj.save(update_fields=["views_count"])
        # Реализуем доп задание.
        # Отправляем email при достижении 10 просмотров.
        if obj.views_count == 10:
            send_mail(
                subject=f'Статья "{obj.title}" набрала 10 просмотров!',
                message=f'Поздравляем! Ваша статья "{obj.title}" достигла 10 просмотров.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Отправляем себе.
                fail_silently=True,
            )

        return obj


# Create - создание статьи.
class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = [
        "title",
        "content",
        "preview",
        "is_published",
    ]
    success_url = reverse_lazy("blog:list")


# Update - обнова, изменение статьи.
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]

    def get_success_url(self):
        # Перенаправляем на детальную страницу отредактированной статьи.
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


# Delete - удаление статьи.
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:list")
