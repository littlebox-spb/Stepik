# Напишите определение функциии sum_numbers
def sum_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Аргумент numbers должен быть списком")
    if len(numbers) == 0:
        raise ValueError("Пустой список")
    try:
        return sum(numbers)
    except:
        raise TypeError("Неправильный тип элемента")


# Ниже код для проверки функциии sum_numbers

for value in (True, (1, 2, 3), {1: "hello"}, {1, 2, 3}):
    try:
        result = sum_numbers(value)
    except TypeError as error:
        print(error)

try:
    result = sum_numbers([])
except ValueError as error:
    print(error)

try:
    sum_numbers([1, "hello", 2, 3])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
except TypeError as error:
    print(error)

assert sum_numbers([1, 2, 3, 4, 5]) == 15
assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0

# class Customer:
#     def __init__(self, name, balance=0) -> None:
#         self.name = name
#         self.balance = balance

#     @staticmethod
#     def check_type(number):
#         if not (isinstance(number, (int, float)) and not isinstance(number, bool)):
#             raise TypeError("Банк работает только с числами")

#     def withdraw(self, dept):
#         self.check_type(dept)
#         if self.balance >= dept:
#             self.balance -= dept
#         else:
#             raise ValueError("Сумма списания превышает баланс")

#     def deposit(self, dept):
#         self.check_type(dept)
#         self.balance += dept


# assert Customer.check_type(2) is None, "Метод check_type не должен ничего возращать"
# assert Customer.check_type(2.5) is None, "Метод check_type не должен ничего возращать"

# for i in ["hello", [1, 2, 3], dict(), set()]:
#     try:
#         Customer.check_type(i)
#     except TypeError as error:
#         print(error)
#     else:
#         raise TypeError(f"Метод check_type должен вызывать ошибку если передать {i}")

# bob = Customer("Bob Odenkirk")
# assert bob.balance == 0
# assert bob.name == "Bob Odenkirk"
# try:
#     bob.deposit("hello")
# except TypeError as error:
#     print(error)
# else:
#     raise ValueError("Нельзя вносить на счет баланса строку")

# try:
#     bob.deposit([])
# except TypeError as error:
#     print(error)
# else:
#     raise ValueError("Нельзя вносить на счет баланса список")

# bob.deposit(200)
# assert bob.balance == 200

# try:
#     bob.withdraw(300)
# except ValueError as e:
#     print(e)
# else:
#     raise ValueError("Проверьте списание при превышении лимита")

# bob.withdraw(150)
# assert bob.balance == 50

# terk = Customer("Terk", 1000)
# assert terk.name == "Terk"
# assert terk.balance == 1000
# terk.withdraw(999)
# assert terk.balance == 1, "Не списались деньги, проверяйте списание"
# terk.withdraw(1)
# assert terk.balance == 0, "Не списались деньги, проверяйте списание"

# try:
#     terk.withdraw(1)
# except ValueError as e:
#     print(e)
# else:
#     raise ValueError("Проверьте списание при превышении лимита")
# assert terk.balance == 0
