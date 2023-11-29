class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} ({self.capacity}L)"

    def __add__(self, other):
        return Juice(f"{self.name}&{other.name}", self.capacity + other.capacity)


a = Juice("Orange", 1.5)
b = Juice("Apple", 2.0)

result = a + b
print(result)


# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator

#     @staticmethod
#     def folding(numerator, denominator):
#         for i in range(2, 7):
#             while numerator % i == 0 and denominator % i == 0:
#                 numerator //= i
#                 denominator //= i
#         return Fraction(numerator, denominator)

#     def __add__(self, other):
#         numerator1 = self.numerator * other.denominator
#         denominator = self.denominator * other.denominator
#         numerator2 = other.numerator * self.denominator
#         return self.folding(numerator1 + numerator2, denominator)

#     def __sub__(self, other):
#         numerator1 = self.numerator * other.denominator
#         denominator = self.denominator * other.denominator
#         numerator2 = other.numerator * self.denominator
#         return self.folding(numerator1 - numerator2, denominator)

#     def __mul__(self, other):
#         numerator1 = self.numerator * other.numerator
#         denominator = self.denominator * other.denominator
#         return self.folding(numerator1, denominator)

#     def __eq__(self, other):
#         return (
#             self.numerator == other.numerator and self.denominator == other.denominator
#         )


# # Примеры использования класса Fraction
# frac1 = Fraction(1, 2)
# frac2 = Fraction(3, 4)

# # Пример сложения дробей
# result = frac1 + frac2
# print(result == Fraction(5, 4))  # ожидаемый вывод: 5/4

# # Пример вычитания дробей
# result = frac1 - frac2
# print(result == Fraction(-1, 4))  # ожидаемый вывод: -1/4

# # Пример умножения дробей
# result = frac1 * frac2
# print(result == Fraction(3, 8))  # ожидаемый вывод: 3/8

# # Пример сравнения дробей
# result = frac1 == frac2
# print(result)  # ожидаемый вывод: False
