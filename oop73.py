from dataclasses import dataclass, field
from os import name


@dataclass
class Promo:
    name: str
    discount: float
    prod: list = field(default_factory=list)


@dataclass(order=True)
class Product:
    name: str
    price: float = field(repr=False)


class Cart:
    def __init__(self):
        self.goods = []
        self.discount = 0

    def add_product(self, other, amt=1):
        for prod in range(len(self.goods)):
            if self.goods[prod][0].name == other.name:
                self.goods[prod][1] += amt
                break
        else:
            self.goods.append([other, amt])

    def get_total(self):
        result = 0
        for s in self.goods:
            result += s[0].price * s[1]
        return result

    def apply_discount(self, discount, prod=[]):
        if 1 <= discount <= 100:
            if prod:
                for s in self.goods:
                    if s[0] in prod:
                        s[0].price *= (100 - discount) / 100
            else:
                if self.discount == 0:
                    self.discount = discount
                    for s in self.goods:
                        s[0].price *= (100 - discount) / 100
                else:
                    for s in self.goods:
                        s[0].price /= (100 - self.discount) / 100
                    self.discount = 0
                    self.apply_discount(discount)
        else:
            raise ValueError("Неправильное значение скидки")

    def apply_promo(self, promo):
        for pr in ACTIVE_PROMO:
            if pr.name == promo:
                self.apply_discount(pr.discount, pr.prod)
                print(f"Промокод {promo} успешно применился")
                break
        else:
            print("Промокода goods не существует")


##################################################################################################
book = Product("Книга", 100.0)
usb = Product("Флешка", 50.0)
pen = Product("Ручка", 10.0)

ACTIVE_PROMO = [
    Promo("new", 20, [pen]),
    Promo("all_goods", 30),
    Promo("sale", 50, [book, usb]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
cart.add_product(book, 5)
cart.add_product(usb, 5)
cart.add_product(usb, 15)
cart.add_product(pen, 2)

print(cart.get_total())

# Применение промокода в 50% на книги и флешки
cart.apply_promo("sale")
print(cart.get_total())
