# catalog/validators.py

from django.core.exceptions import ValidationError


# Валидатор для поля name, details.
def validate_stop_words(value):
    """Проверка на запрещенные слова в тексте."""

    stop_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    # Приводим значение к нижнему регистру для проверки.
    value_lower = value.lower()

    # Проверяем наличие каждого запрещенного слова в цикле.
    for word in stop_words:
        if word in value_lower:
            raise ValidationError(f"Запрещено использовать слово <<{word}>> в этом поле.")

    return value


# Валидатор для поля price.
def validate_price(check_price):
    """Проверка цены - что она не отрицательная."""
    if check_price < 0:
        raise ValidationError("Отрицательная цена? Это не благотворительность!")
    elif check_price == 0:
        raise ValidationError("Бесплатно не отдаём, введите реальную цену!")


# Валидатор для поля img.
def validate_image(image):
    """Проверка формата и размера изображения."""

    # Пропускаем проверку, если это уже сохранённый файл (при редактировании)
    if not hasattr(image, "content_type"):
        return

    # Проверка размера файла (5 МБ = 5 * 1024 * 1024 байт).
    max_size = 5 * 1024 * 1024  # 5 МБ.
    if image.size > max_size:
        raise ValidationError(f"Файл не больше 5 МБ. Ваш файл: {image.size / (1024 * 1024):.2f} МБ")

    # Проверка формата файла.
    allowed_formats = ["image/jpeg", "image/png", "image/jpg"]
    if image.content_type not in allowed_formats:
        raise ValidationError("Разрешены форматы JPEG и PNG")
