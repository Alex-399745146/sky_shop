# sky_shop

Учебный проект интернет-магазина на Django.

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
poetry run python manage.py migrate

# Создание суперпользователя для админки
poetry run python manage.py createsuperuser

# Запуск сервера разработки
poetry run python manage.py runserver
```

## Управление данными

### Загрузка тестовых данных

```bash
# Загрузка через кастомную команду
poetry run python manage.py add_products

# Загрузка из фикстур
poetry run python manage.py loaddata catalog/fixtures/categories.json
poetry run python manage.py loaddata catalog/fixtures/products.json
```

### Экспорт данных

```bash
# Экспорт в UTF-8 (для Windows)
python export_fixtures.py

# Экспорт категорий
poetry run python manage.py dumpdata catalog.Category --indent 4 -o catalog/fixtures/categories.json

# Экспорт продуктов
poetry run python manage.py dumpdata catalog.Product --indent 4 -o catalog/fixtures/products.json
```
## Функциональность

### Приложение catalog
- Модели: `Category` (категории товаров), `Product` (товары)
- Список товаров с изображениями и ценами
- Детальная страница товара
- Фильтрация по категориям
- Страница контактов

### Шаблоны
- Базовый шаблон с Bootstrap 5
- Адаптивная вёрстка
- Компонентная структура (includes)
- Шаблонные фильтры для обрезки текста

### Админ-панель
- Управление категориями
- Управление товарами
- Загрузка изображений

## Доступные URL

| URL | Название | Описание |
|-----|----------|----------|
| `/` | `catalog:catalog_list` | Главная страница (список товаров) |
| `/product/<int:pk>/` | `catalog:product_detail` | Детальная страница товара |
| `/contacts/` | `catalog:contacts` | Страница контактов |
| `/admin/` | — | Админ-панель Django |

## Запуск через Poetry

```bash
# Активация окружения
poetry shell

# Запуск сервера
python manage.py runserver

# Или без активации
poetry run python manage.py runserver
```

## Разработка

```bash
# Создание миграций после изменения моделей
poetry run python manage.py makemigrations

# Применение миграций
poetry run python manage.py migrate

# Запуск shell для отладки
poetry run python manage.py shell

# Сбор статики (для продакшена)
poetry run python manage.py collectstatic
```

## Git

```bash
# ✅ Коммитить:
# - Файлы миграций (catalog/migrations/*.py)
# - Фикстуры (catalog/fixtures/*.json)

# ❌ НЕ коммитить:
# - db.sqlite3 (база данных)
# - __pycache__/
# - .env (секретные данные)
```

## ⚠️ Важно: Медиа файлы в репозитории

> **Папка `media/` включена в репозиторий ТОЛЬКО для учебных целей!**
> 
> В реальных проектах медиа файлы (загрузки пользователей) **НЕ коммитятся** в Git и добавляются в `.gitignore`.
> Обычно они хранятся на внешних сервисах (AWS S3, Cloudinary и т.д.).
> 
> Здесь файлы добавлены для демонстрации и упрощения развёртывания учебного проекта.

```bash
# В production проектах:
# echo "media/" >> .gitignore
# git rm -r --cached media/
```

## Автор
**Alex Bachevskiy**  
Инженер-программист Python | SkyPro

---

*Учебный проект курса Python-разработчик*
