import os
from pathlib import Path

from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv(override=True, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1", "0.0.0.0"]

INSTALLED_APPS = [
    # Встроенные приложения.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Мои зарегистрированные приложения.
    # "django_bootstrap5",  # Подключение стилей по CDN.
    "django_extensions",
    "catalog",  # Приложение_1.
    "blog",  # Приложение_2.
    "users",  # Приложение_3.
]

AUTH_USER_MODEL = "users.User"  # Django для авторизации используй эту модель.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sky_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sky_shop.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = False  # отключает локализованное форматирование дат, чисел и времени.

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# MEDIA файлы (загрузка изображений)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Настройки почты (для разработки - вывод в консоль)
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# DEFAULT_FROM_EMAIL = "noreply@skystore.ru"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Для реальной отправки (например, через Yandex):

# Для реальной отправки:
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

LOGIN_URL = "users:login"
# Редирект для перенаправлений после входа и выхода.
LOGIN_REDIRECT_URL = "catalog:product_list"
LOGOUT_REDIRECT_URL = "catalog:product_list"

# Настройки кэша.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
