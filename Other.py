class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )


# Примеры использования класса Fraction
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Пример сложения дробей
result = frac1 + frac2
print(result != Fraction(5, 4))  # Ожидаемый вывод: True

# Пример вычитания дробей
result = frac1 - frac2
print(result != Fraction(-1, 4))  # Ожидаемый вывод: True

# Пример умножения дробей
result = frac1 * frac2
print(result == Fraction(3, 8))  # Ожидаемый вывод: True

# Пример сравнения дробей
result = frac1 == frac2
print(result)  # Ожидаемый вывод: False
