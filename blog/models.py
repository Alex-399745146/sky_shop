from django.db import models


class BlogPost(models.Model):
    """Класс модели постов в блоге(чате)."""

    # Основные поля (обязательные для заполнения).
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
    )

    content = models.TextField(
        verbose_name="Содержимое",
    )

    # Дополнительные поля (необязательные).
    preview = models.ImageField(
        upload_to="blog_previews/",
        blank=True,
        null=True,
        default="blog_previews/preview.jpeg",
        verbose_name="Превью (изображение)",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )

    # Служебные поля (автоматические).
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    views_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.title

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "запись блога"
        verbose_name_plural = "записи блога"
        ordering = ["-created_at"]  # Сортировка.
