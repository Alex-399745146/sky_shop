# catalog/forms.py

from django import forms
from catalog.models import Product
from catalog.validators import validate_stop_words, validate_price


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта."""

    class Meta:
        model = Product
        fields = ['name', 'details', 'img', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта'
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Введите описание продукта'
            }),
            'img': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01',
                'placeholder': '0.00'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем валидатор к полям name и details.
        self.fields['name'].validators.append(validate_stop_words)
        self.fields['details'].validators.append(validate_stop_words)

    def clean_name(self):
        """Валидация поля name."""
        name = self.cleaned_data.get('name')
        return validate_stop_words(name)

    def clean_details(self):
        """Валидация поля details."""
        details = self.cleaned_data.get('details')
        return validate_stop_words(details)

    def clean_price(self):
        """Валидация поля price."""
        check_price = self.cleaned_data.get('price')
        validate_price(check_price)
        return check_price


class ContactForm(forms.Form):
    """Форма обратной связи."""

    name = forms.CharField(
        max_length=100,
        label='Имя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        })
    )
    phone = forms.CharField(
        max_length=20,
        label='Телефон',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+7 (999) 123-45-67'
        })
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Ваше сообщение'
        })
    )
