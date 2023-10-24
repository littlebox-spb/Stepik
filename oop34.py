# Напишите определение класса Rectangle
from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, (int, float)):
            return self.area == __value
        if isinstance(__value, Rectangle):
            return self.area == __value.area

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, (int, float)):
            return self.area < __value
        if isinstance(__value, Rectangle):
            return self.area < __value.area


# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), "Вы не создали property area"

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print("Good")

# # Напишите определение класса ChessPlayer
# class ChessPlayer:
#     def __init__(self, name, surname, rating) -> None:
#         self.name = name
#         self.surname = surname
#         self.rating = rating

#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.rating == other
#         elif isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         return "Невозможно выполнить сравнение"

#     def __gt__(self, other):
#         if isinstance(other, int):
#             return self.rating > other
#         elif isinstance(other, ChessPlayer):
#             return self.rating > other.rating
#         return "Невозможно выполнить сравнение"

#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.rating < other
#         elif isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         return "Невозможно выполнить сравнение"


# # Ниже код для проверки методов класса ChessPlayer
# magnus = ChessPlayer("Carlsen", "Magnus", 2847)
# assert magnus.name == "Carlsen"
# assert magnus.surname == "Magnus"
# assert magnus.rating == 2847
# ian = ChessPlayer("Ian", "Nepomniachtchi", 2789)
# assert not magnus == 4000
# assert ian == 2789
# assert not magnus == ian
# assert magnus > ian
# assert not magnus < ian
# assert (magnus < [1, 2]) == "Невозможно выполнить сравнение"

# v1 = ChessPlayer("Гарри ", "Каспаров", 10)
# v2 = ChessPlayer("Бобби", "Фишер", 20)
# v3 = ChessPlayer("Bot", "Bot", 20)

# assert isinstance(v1, ChessPlayer)
# assert isinstance(v2, ChessPlayer)
# assert v2.__dict__ == {"name": "Бобби", "surname": "Фишер", "rating": 20}
# assert v1.__dict__ == {"name": "Гарри ", "surname": "Каспаров", "rating": 10}
# assert v1 > 5
# assert not v1 > 10
# assert not v1 > 11
# assert not v1 < 5
# assert not v1 < 10
# assert v1 < 11
# assert not v1 == 5
# assert v1 == 10
# assert not v1 == 11
# assert not v1 > v2
# assert not v1 == v2
# assert v3 == v2
# assert not v3 != v2
# assert v1 < v2
# assert (v1 > "fdsfd") == "Невозможно выполнить сравнение"
# assert (v1 < "fdsfd") == "Невозможно выполнить сравнение"
# assert (v1 == "fdsfd") == "Невозможно выполнить сравнение"
# assert (v1 == [1, 2]) == "Невозможно выполнить сравнение"
# assert (v1 < [1, 2]) == "Невозможно выполнить сравнение"
# print("Good")

# # Напишите определение класса Fruit
# class Fruit:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price

#     def __gt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.price > other
#         return isinstance(other, Fruit) and self.price > other.price

#     def __ge__(self, other):
#         if isinstance(other, (int, float)):
#             return self.price >= other
#         return isinstance(other, Fruit) and self.price >= other.price

#     def __lt__(self, other):
#         if isinstance(other, (int, float)):
#             return self.price < other
#         return isinstance(other, Fruit) and self.price < other.price

#     def __le__(self, other):
#         if isinstance(other, (int, float)):
#             return self.price <= other
#         return isinstance(other, Fruit) and self.price <= other.price

#     def __eq__(self, other):
#         return isinstance(other, Fruit) and self.price == other.price


# # Ниже код для проверки методов класса Fruit

# apple = Fruit("Apple", 0.5)
# orange = Fruit("Orange", 1)
# banana = Fruit("Banana", 1.6)
# lime = Fruit("Lime", 1.0)

# assert (banana > 1.2) is True
# assert (banana >= 1.2) is True
# assert (banana == 1.2) is False
# assert (banana != 1.2) is True
# assert (banana < 1.2) is False
# assert (banana <= 1.2) is False

# assert (apple > orange) is False
# assert (apple >= orange) is False
# assert (apple == orange) is False
# assert (apple != orange) is True
# assert (apple < orange) is True
# assert (apple <= orange) is True

# assert (orange == lime) is True
# assert (orange != lime) is False
# assert (orange > lime) is False
# assert (orange < lime) is False
# assert (orange <= lime) is True
# assert (orange >= lime) is True
# print("Good")
