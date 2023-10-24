# Напишите определение класса Quadrilateral
class Quadrilateral:
    def __init__(self, width, height=0) -> None:
        self.width = width
        self.height = width if height == 0 else height

    def __str__(self) -> str:
        return (
            f"Квадрат размером {self.width}х{self.width}"
            if self.height == self.width
            else f"Прямоугольник размером {self.width}х{self.height}"
        )

    def __bool__(self) -> bool:
        return self.height == self.width


# Ниже код для проверки методов класса Quadrilateral

q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)

# # Напишите определение класса City
# class City:
#     def __init__(self, name) -> None:
#         self.name = name.title()

#     def __str__(self) -> str:
#         return self.name

#     def __bool__(self) -> bool:
#         return not (self.name[-1] in ("a", "e", "i", "o", "u"))


# # Ниже код для проверки методов класса City

# p1 = City("new york")
# assert p1.name == "New York"
# assert p1.__str__() == "New York"
# assert isinstance(p1, City)
# print(p1)
# assert bool(p1)

# p2 = City("SaN frANCISco")
# assert isinstance(p2, City)
# assert p2.name == "San Francisco"
# print(p2)
# assert not bool(p2)

# p3 = City("NIZHNY NoVGORod")
# assert p3.name == "Nizhny Novgorod"
# print(p3)
# assert bool(p3)
# assert isinstance(p3, City)
