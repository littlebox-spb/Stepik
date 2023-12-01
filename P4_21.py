from math import pi


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

    def calculate_perimeter(self):
        return pi * self.radius * 2


# Тесты
rectangle = Rectangle(5, 7)
assert rectangle.calculate_area() == 35
assert rectangle.calculate_perimeter() == 24

circle = Circle(3)
assert round(circle.calculate_area(), 2) == 28.27
assert round(circle.calculate_perimeter(), 2) == 18.85

print("Тесты пройдены успешно!")
