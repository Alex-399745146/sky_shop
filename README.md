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
- Фильтрация по категориям  
- Контакты + вывод последней статьи блога на главной

### Blog

- Модель `BlogPost`, полный CRUD  
- Счётчик просмотров + фильтр по `is_published`  
- Email-уведомление при 100+ просмотрах  
- Превью изображений с дефолтом

### Users

- Кастомный `User` с логином по email (без username).  
- Профиль: аватар, телефон, страна, токен для подтверждения.  
- Регистрация с email-подтверждением ссылки до активации аккаунта.  
- Вход/выход, редирект после logout на главную, отображение «Вы вошли как \<email\>» в шапке.

### UI и шаблоны

- Базовый шаблон на Bootstrap 5  
- Фиксированный navbar (`fixed-top`) + кнопки входа/выхода.  
- Адаптивная сетка карточек: 1 / 2 / 3 в ряд в зависимости от ширины экрана.  
- «Липкий» footer, всегда внизу окна (flex + `min-vh-100`).  
- Компонентные include-шаблоны.

## Важные URL

- `/` — список товаров + последняя статья (`catalog:product_list`)  
- `/product/<pk>/` — товар (`catalog:product_detail`)  
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

Для реальной отправки — включить SMTP-настройки в `settings.py`.

## Git и медиа

- Коммитим миграции и фикстуры.  
- Не коммитим: `__pycache__/`, `.env`, `media/` (кроме учебной цели).  
- `media/` в репозитории только для обучения, в production обычно S3/Cloudinary и т.п.

## Автор

**Alex Bachevskiy**  
Инженер-программист Python | SkyPro  

*Учебный проект курса «Python-разработчик»*