# blog/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # Ленивое динамичное формирование адреса.
from blog.models import BlogPost


# Read - весь список.
class BlogPostListView(ListView):
    model = BlogPost


# Read - детально статью.
class BlogPostDetailView(DetailView):
    model = BlogPost


# Create - создание статьи.
class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published',]
    success_url = reverse_lazy('blog:list')


# Update - обнова, изменение статьи.
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')


# Delete - удаление статьи.
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')
