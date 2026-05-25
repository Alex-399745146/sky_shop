# catalog/validators.py

from django.core.exceptions import ValidationError


def validate_stop_words(value):
    """Проверка на запрещенные слова в тексте."""

    stop_words = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар',
    ]

    # Приводим значение к нижнему регистру для проверки.
    value_lower = value.lower()

    # Проверяем наличие каждого запрещенного слова в цикле.
    for word in stop_words:
        if word in value_lower:
            raise ValidationError(
                f'Запрещено использовать слово "{word}" в этом поле.'
            )

    return value
