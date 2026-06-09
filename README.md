# sky_shop

Учебный интернет-магазин на Django с каталогом, блогом и пользователями.

## Стек

- Python 3.13, Django 4.2, PostgreSQL  
- Poetry, Bootstrap 5.2, Pillow

## Установка

```bash
git clone <url>
cd sky_shop

poetry install
poetry shell

cp .env.example .env  # настроить доступ к БД
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Основные возможности

### Catalog

- Модели `Category`, `Product`
- Список и детальная страница товара
- Флаг публикации `is_published` — в каталоге видны только опубликованные товары
- Владелец товара (`owner`) привязывается к авторизованному пользователю
- Редактировать товар может только его владелец
- Удалять товар может владелец или модератор (через группу и права)
- Модераторы могут снимать товар с публикации (кастомное право `can_unpublish_product`)
- Контакты + вывод последней статьи блога на главной

### Blog

- Модель `BlogPost`, полный CRUD
- Счётчик просмотров + фильтр по `is_published`
- Email-уведомление при 100+ просмотрах
- Превью изображений с дефолтом

### Users

- Кастомный `User` с логином по email (без username)
- Профиль: аватар, телефон, страна, токен для подтверждения
- Регистрация с email-подтверждением до активации аккаунта
- Вход/выход, редирект после logout на главную
- В шапке отображается «Вы вошли как <email>»

### Права и роли

- Стандартные права Django (`add/change/delete/view`) на модели
- Кастомное право `can_unpublish_product` для модели `Product`
- Группа «Модераторы» с правами на удаление и снятие с публикации товаров
- Шаблоны и контроллеры проверяют права: кнопки действий видны только тем, кто может их выполнять [web:625][web:690]

### UI и шаблоны

- Базовый шаблон на Bootstrap 5
- Фиксированный navbar (`fixed-top`) + кнопки входа/выхода
- Адаптивная сетка карточек: 1 / 2 / 3 в ряд
- «Липкий» footer (flex + `min-vh-100`)
- Компонентные include-шаблоны

## Важные URL

- `/` — список товаров + последняя статья (`catalog:product_list`)
- `/product/<pk>/` — товар (`catalog:product_detail`)
- `/product/create/` — создание товара (только авторизованные, владелец проставляется автоматически)
- `/contacts/` — контакты (`catalog:contacts`)
- `/blog/` и CRUD по блог-постам (`blog:*`)
- `/users/login/`, `/users/logout/`, `/users/register/`, `/users/email-confirm/<token>/` (`users:*`)
- `/admin/` — админка

## Данные

```bash
# Загрузка тестовых данных
python manage.py add_products
python manage.py loaddata catalog/fixtures/categories.json
python manage.py loaddata catalog/fixtures/products.json

# Экспорт
python manage.py dumpdata catalog.Category --indent 4 -o catalog/fixtures/categories.json
python manage.py dumpdata catalog.Product --indent 4 -o catalog/fixtures/products.json
python manage.py dumpdata blog.BlogPost --indent 4 -o blog/fixtures/blogposts.json
```

## Email

По умолчанию:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Для реальной отправки — включить SMTP-настройки в `.env` / `settings.py`.

## Git и медиа

- Коммитим миграции и фикстуры
- Не коммитим: `__pycache__/`, `.env`, `media/` (кроме учебной цели)
- В продакшене медиа обычно выносятся во внешнее хранилище (S3/Cloudinary и т.п.)

## Автор

**Alex Bachevskiy**  
Инженер-программист Python | SkyPro  

*Учебный проект курса «Python-разработчик»*