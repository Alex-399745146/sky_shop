"""
Модели приложения catalog.
Содержит модели Category и Product для управления каталогом товаров.
Много лишних комментариев ДА знаю это для запоминания!
"""

from django.conf import settings
from django.db import models


class Category(models.Model):
    """Класс модели категории товаров."""

    name = models.CharField(
        max_length=100,  # Ограничение длины текста.
        verbose_name="Наименование",  # Читаемое имя в админке/формах.
    )
    description = models.TextField(
        default="Описание отсутствует",  # Значение по умолчанию.
        verbose_name="Описание категории",  # Читаемое имя в админке/формах.
    )

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.name

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "Категория"  # Имя в единственном числе.
        verbose_name_plural = "Категории"  # Имя во множественном числе.
        ordering = ["name"]  # Сортировка по алфавиту.


class Product(models.Model):
    """Класс модели карточек товара в каталоге."""

    name = models.CharField(
        max_length=200,  # Ограничение длины текста.
        verbose_name="Наименование",  # Читаемое имя в админке/формах.
    )

    details = models.TextField(
        default="Описание отсутствует",  # Значение по умолчанию.
        verbose_name="Описание продукта",  # Читаемое имя в админке/формах.
    )

    img = models.ImageField(
        upload_to="products/",  # Папка загрузки в MEDIA_ROOT.
        blank=True,  # Необязательное в формах Django.
        null=True,  # Может быть NULL в БД PostgreSQL.
        verbose_name="Изображение",  # Читаемое имя в админке/формах.
        help_text="Загрузи фото товара",
    )

    category = models.ForeignKey(
        Category,  # Связь с моделью Category.
        on_delete=models.CASCADE,  # При удалении категории -> удалить товары.
        related_name="products",  # Обратная связь: category.products.all().
        verbose_name="Категория",  # Читаемое имя в админке/формах.
    )

    price = models.DecimalField(  # FloatField - ошибки округления -> DecimalField.
        max_digits=10,  # Всего цифр (включая дробную часть).
        decimal_places=2,  # Цифр после запятой (копейки).
        verbose_name="Цена за покупку",  # Читаемое имя в админке/формах.
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Автоматически при создании.
        verbose_name="Дата создания",  # Читаемое имя в админке/формах.
    )

    updated_at = models.DateTimeField(
        auto_now=True,  # Автоматически при каждом сохранении.
        verbose_name="Дата последнего изменения",  # Читаемое имя в админке/формах.
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Ссылка на кастомного пользователя без жёткой привязки к классу.
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Кто создал эту карточку товара",
        related_name="products",  # user.products.all()
        null=True,
        blank=True,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.name

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "Продукт"  # Имя в единственном числе.
        verbose_name_plural = "Продукты"  # Имя во множественном числе.
        ordering = ["-created_at"]  # Сортировка от новых к старым.

        # Добавим кастомное право изменять поле публикации.
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
