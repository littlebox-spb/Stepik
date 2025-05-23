class Product:
    """Товар (может существовать без заказа)"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Payment:
    """Оплата (не существует без заказа - композиция)"""

    def __init__(self, amount):
        self.amount = amount
        self.paid = False

    def process_payment(self):
        self.paid = True
        return f"Оплачено {self.amount} руб."


class Order:
    """Заказ (использует агрегацию для товаров и композицию для оплаты)"""

    def __init__(self):
        self.products = []  # Агрегация (товары могут существовать без заказа)
        self.payment = None  # Композиция (оплата не существует без заказа)

    def add_product(self, product):
        self.products.append(product)

    def create_payment(self):
        total = sum(p.price for p in self.products)
        self.payment = Payment(total)  # Создаем объект оплаты
        return self.payment


# Пример использования:

# Создаем товары (существуют независимо от заказов)
laptop = Product("Ноутбук", 50000)
phone = Product("Телефон", 30000)

# Создаем заказ
order = Order()
order.add_product(laptop)
order.add_product(phone)

# Создаем и обрабатываем оплату
payment = order.create_payment()
print(payment.process_payment())  # "Оплачено 80000 руб."

# Товары продолжают существовать после удаления заказа
del order
print(laptop.name)  # "Ноутбук" (все еще доступен)
