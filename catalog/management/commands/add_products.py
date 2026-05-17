"""
Кастомная команда для загрузки тестовых данных в БД.
Команда удаляет все существующие категории и продукты,
затем создаёт новые тестовые данные для разработки и тестирования.
Для использования команда: poetry run python manage.py add_products
"""

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Создание класса для нашей команды"""

    help = "Обнуляет БД и записывает тестовые данные в БД."  # Атрибут help описывает что делает команда.

    #  В методе handle описан основной код(логика) нашей команды(макроса).
    def handle(self, *args, **kwargs):

        # 1. Удаляем существующие данные.
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2.1. Создаём категорию электроники.
        electronics = Category.objects.create(name="Электроника", description="Гаджеты и техника")

        # 2.2. Создаём категорию одежды.
        clothing = Category.objects.create(name="Одежда", description="Одежда и модные аксессуары")

        # 3. Создаём-добавляем продукты в БД.
        products = [
            {"name": "iPhone 15", "details": "Смартфон Apple", "category": electronics, "price": 115000.00},
            {"name": "MacBook Pro", "details": "Ноутбук Apple", "category": electronics, "price": 250000.00},
            {"name": "Трико", "details": "Классические штаны", "category": clothing, "price": 500.00},
            {"name": "Куртка Nike", "details": "Спортивная куртка", "category": clothing, "price": 12000.00},
        ]

        # Добавляем продукты через цикл с проверкой.
        for product_data in products:
            # created => True(False) метод .get_or_create() так устроен.
            product, created = Product.objects.get_or_create(**product_data)
            # stdout.write - перехват в вывод терминала(ну и статус важности сообщения).
            if created:
                self.stdout.write(self.style.SUCCESS(f"Добавлен продукт: {product.name} - {product.price} руб."))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт уже существует: {product.name}"))

        self.stdout.write(self.style.SUCCESS(f"\nВсего обработано: {len(products)} продуктов"))
