# users/views.py

import secrets

from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm  # Сделаем сразу ниже.
from .models import User
from django.conf import settings


class UserLoginView(LoginView):
    template_name = "users/login.html"  # шаблон логина
    # По умолчанию ожидает поля USERNAME_FIELD (у нас email) и password.


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("catalog:product_list")  # Куда редиректить после выхода.


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")  # После регистрации переход на вход логин.

    # Переопределяем метод валидации формы.
    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)  # Генерация токена.
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/" # Ссылка для пользователя на почту.
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылки для подтверждения почты {url}.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
