# sky_shop

Учебный проект интернет-магазина на Django с блогом и каталогом товаров.

## Технологии
- Python 3.13
- Django 4.2
- Poetry (управление зависимостями)
- Bootstrap 5.2 (фронтенд)
- PostgreSQL (база данных)
- Pillow (обработка изображений)

## Установка

```bash
# Клонирование репозитория
git clone <url>
cd sky_shop

# Установка зависимостей через Poetry
poetry install

# Активация виртуального окружения
poetry shell

# Настройка переменных окружения
cp .env.example .env
# Отредактируй .env и укажи параметры подключения к PostgreSQL

# Применение миграций
python manage.py migrate

# Создание суперпользователя для админки
python manage.py createsuperuser

# Запуск сервера разработки
python manage.py runserver
```

## Функциональность

### Приложение catalog
- **Модели**: `Category`, `Product`
- Список товаров с изображениями и ценами
- Детальная страница товара
- Фильтрация по категориям
- Страница контактов
- Отображение последней статьи блога на главной

### Приложение blog
- **Модель**: `BlogPost`
- CRUD операции для статей
- Счётчик просмотров
- Фильтр публикации (is_published)
- Email-уведомление при достижении 100 просмотров
- Превью изображений с дефолтным значением

### Шаблоны
- Базовый шаблон с Bootstrap 5
- Адаптивная вёрстка
- Компонентная структура (includes)
- Шаблонные фильтры

### Админ-панель
- Управление категориями и товарами
- Управление статьями блога
- Загрузка изображений

## Доступные URL

| URL | Название | Описание |
|-----|----------|----------|
| `/` | `catalog:catalog_list` | Главная (список товаров + последняя статья) |
| `/product/<int:pk>/` | `catalog:product_detail` | Детальная страница товара |
| `/contacts/` | `catalog:contact` | Страница контактов |
| `/blog/` | `blog:list` | Список статей блога |
| `/blog/<int:pk>/` | `blog:detail` | Детальная страница статьи |
| `/blog/create/` | `blog:create` | Создание статьи |
| `/blog/<int:pk>/update/` | `blog:update` | Редактирование статьи |
| `/blog/<int:pk>/delete/` | `blog:delete` | Удаление статьи |
| `/admin/` | — | Админ-панель Django |

## Управление данными

### Загрузка тестовых данных

```bash
# Загрузка через кастомную команду
python manage.py add_products

# Загрузка из фикстур
python manage.py loaddata catalog/fixtures/categories.json
python manage.py loaddata catalog/fixtures/products.json
```

### Экспорт данных

```bash
# Экспорт в UTF-8 (для Windows)
python export_fixtures.py

# Экспорт категорий
python manage.py dumpdata catalog.Category --indent 4 -o catalog/fixtures/categories.json

# Экспорт продуктов
python manage.py dumpdata catalog.Product --indent 4 -o catalog/fixtures/products.json

# Экспорт статей блога
python manage.py dumpdata blog.BlogPost --indent 4 -o blog/fixtures/blogposts.json
```

## Разработка

```bash
# Создание миграций после изменения моделей
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Запуск shell для отладки
python manage.py shell

# Сбор статики (для продакшена)
python manage.py collectstatic
```

## Email уведомления

По умолчанию используется консольный бэкенд — письма выводятся в терминал.

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Для реальной отправки раскомментируй SMTP-настройки в `settings.py`.

## Git

```bash
# ✅ Коммитить:
# - Файлы миграций (*/migrations/*.py)
# - Фикстуры (*/fixtures/*.json)

# ❌ НЕ коммитить:
# - db.sqlite3
# - __pycache__/
# - .env
# - media/ (кроме учебных проектов)
```

## ⚠️ Важно: Медиа файлы

> Папка `media/` включена в репозиторий **ТОЛЬКО для учебных целей**.
> 
> В production медиа файлы хранятся на внешних сервисах (S3, Cloudinary).

## Автор
**Alex Bachevskiy**  
Инженер-программист Python | SkyPro

---

*Учебный проект курса Python-разработчик*