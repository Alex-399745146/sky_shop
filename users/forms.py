# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    """Форма регистрации пользователя с полями: email, пароль, телефон, страна, аватар."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "avatar",
            "phone",
            "country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Простая стилизация полей Bootstrap-классами.
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
