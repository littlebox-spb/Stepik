# Напишите определение класса GroceryItem
class GroceryItem:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"

    def __repr__(self) -> str:
        return f"GroceryItem({self.name}, {self.price}, {self.quantity})"


# Ниже код для проверки методов класса GroceryItem
banana = GroceryItem("Banana", 10, 5)
assert (
    banana.__str__()
    == """Name: Banana
Price: 10
Quantity: 5"""
)
assert repr(banana) == "GroceryItem(Banana, 10, 5)"
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem("Dragon fruit", 5, 350)
assert (
    dragon_fruit.__str__()
    == """Name: Dragon fruit
Price: 5
Quantity: 350"""
)
assert repr(dragon_fruit) == "GroceryItem(Dragon fruit, 5, 350)"
print(dragon_fruit)
print(f"{dragon_fruit!r}")

# # Напишите определение класса Vector
# class Vector:
#     def __init__(self, *args) -> None:
#         self.values = []
#         for n in args:
#             if isinstance(n, int) and not isinstance(n, bool):
#                 self.values.append(n)

#     def __str__(self) -> str:
#         if len(self.values) == 0:
#             return "Пустой вектор"
#         else:
#             return "Вектор(" + ", ".join(map(str, sorted(self.values))) + ")"


# # Ниже код для проверки методов класса Vector

# v1 = Vector(1, 2, 3)
# assert isinstance(v1, Vector)
# assert str(v1) == "Вектор(1, 2, 3)"

# v2 = Vector()
# assert isinstance(v2, Vector)
# assert str(v2) == "Пустой вектор"

# v3 = Vector([4, 5], "hello", 3, -1.5, 1, 2)
# assert isinstance(v3, Vector)
# assert sorted(v3.values) == [1, 2, 3]
# assert str(v3) == "Вектор(1, 2, 3)"

# v4 = Vector([4, 5], "hello")
# assert str(v2) == "Пустой вектор"
# assert v2.values == []

# v5 = Vector(1, 2, True)
# assert isinstance(v5, Vector)
# assert str(v5) == "Вектор(1, 2)"

# print(v1)
# print(v2)
# print(v3)
# print(v4)

# # # Напишите определение класса Person
# # class Person:
# #     def __init__(self, name, surname, gender="male"):
# #         if gender not in ("male", "female"):
# #             self.gender = "male"
# #             print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
# #         else:
# #             self.gender = gender
# #         self.name = name
# #         self.surname = surname

# #     def __str__(self):
# #         if self.gender == "male":
# #             return f"Гражданин {self.surname} {self.name}"
# #         else:
# #             return f"Гражданка {self.surname} {self.name}"


# # # Ниже код для проверки методов класса Person
# # p1 = Person("Chuck", "Norris")
# # assert p1.name == "Chuck"
# # assert p1.surname == "Norris"
# # assert p1.gender == "male"
# # assert isinstance(p1, Person)
# # assert str(p1) == "Гражданин Norris Chuck"

# # p2 = Person("Оби-Ван", "Кеноби", True)  #  нужно распечатать предупреждение из условия
# # assert str(p2) == "Гражданин Кеноби Оби-Ван"
# # assert p2.__dict__ == {"name": "Оби-Ван", "surname": "Кеноби", "gender": "male"}
# # assert isinstance(p2, Person)

# # p3 = Person("Mila", "Kunis", "female")
# # assert isinstance(p3, Person)
# # assert str(p3) == "Гражданка Kunis Mila"

# # print(p1)
# # print(p2)
# # print(p3)
