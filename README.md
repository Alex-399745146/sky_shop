# sky_shop

Учебный проект интернет-магазина на Django.

## Технологии
- Python 3.13
- Django 4.2
- Poetry (управление зависимостями)
- Bootstrap 5 (вёрстка)
- PostgreSQL (база данных)

## Установка

```bash
# Клонирование
git clone <url>
cd sky_shop

# Установка зависимостей
poetry install

# Активация окружения
poetry shell

# Настройка переменных окружения
cp .env.example .env
# Отредактируй .env и укажи параметры БД

# Миграции БД
poetry run python manage.py migrate

# Создание суперпользователя
poetry run python manage.py createsuperuser

# Запуск сервера
poetry run python manage.py runserver
```

## Управление данными

### Загрузка тестовых данных

```bash
# Загрузка через кастомную команду
poetry run python manage.py add_products

# Загрузка из фикстур
poetry run python manage.py loaddata data.json
```

### Экспорт данных

```bash
# Экспорт в UTF-8 (Windows)
python export_fixtures.py

# Экспорт категорий
poetry run python manage.py dumpdata catalog.Category --indent 4 > catalog/fixtures/categories.json

# Экспорт продуктов
poetry run python manage.py dumpdata catalog.Product --indent 4 > catalog/fixtures/products.json
```

## Структура

```markdown
sky_shop/
├── catalog/                    # Приложение каталога
│   ├── management/
│   │   └── commands/
│   │       └── add_products.py # Кастомная команда загрузки данных
│   ├── fixtures/               # Фикстуры для тестовых данных
│   ├── models.py
│   └── views.py
├── templates/                  # HTML-шаблоны
├── sky_shop/                   # Настройки проекта
├── export_fixtures.py          # Скрипт экспорта в UTF-8
└── manage.py
```

## Приложения
- **catalog** — каталог товаров и категорий, контакты

## Адреса
- Главная: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Каталог: [http://127.0.0.1:8000/catalog/](http://127.0.0.1:8000/catalog/)
- Контакты: [http://127.0.0.1:8000/contacts/](http://127.0.0.1:8000/contacts/)
- Админ-панель: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Автор
Alex Bachevskiy