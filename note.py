# num = 0
# for n in range(5):
#     for i in range(1, 11):
#         print(num + i, end=" ")
#     num += 10
#     print("\n+----+----+----+----+----+----+----+----+----+----+")
#     for i in range(10, 0, -1):
#         print(f"|{num + i}", end=" ")
#     num += 10
#     print("\n+----+----+----+----+----+----+----+----+----+----+")
import math


class Shape:
    def calculate_area(self):
        return 0

    def __add__(self, other):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


shapes = [Shape(), Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    area = shape.calculate_area()
    print(f"Area of {type(shape).__name__}: {area}")
