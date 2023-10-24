import time
from typing import Any


class Timer:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start = time.time()
        self.func()
        print(f"Время работы программы {time.time()-start}")
        return


@Timer
def calculate():
    for i in range(10000000):
        2**100


calculate()

# # Напишите определение класса Addition
# from typing import Any


# class Addition:
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         summa = 0
#         for n in args:
#             if isinstance(n, (int, float)):
#                 summa += n
#             # elif isinstance(n, list):
#             #     for i in n:
#             #         if isinstance(i, (int, float)):
#             #             summa += i
#         return f"Сумма переданных значений = {summa}"


# # Ниже код для проверки методов класса Addition
# add = Addition()
# assert add(10, 20) == "Сумма переданных значений = 30"
# assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
# assert add(1, 2, "hello", [1, 2], 3) == "Сумма переданных значений = 6"


# add2 = Addition()
# assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
# assert add2() == "Сумма переданных значений = 0"
# assert add2("hello") == "Сумма переданных значений = 0"

# print("Good")

# # Напишите определение класса QuadraticFunction
# class QuadraticFunction:
#     def __init__(self, a, b, c) -> None:
#         self.a = a
#         self.b = b
#         self.c = c

#     def __call__(self, x):
#         return self.a * x * x + self.b * x + self.c


# # Ниже код для проверки методов класса QuadraticFunction

# f = QuadraticFunction(2, 5, 7)
# assert f(1) == 14
# assert f(-3) == 10
# assert f(2) == 25
# assert f(5) == 82

# f_2 = QuadraticFunction(-1, 2, 4)
# assert f_2(5) == -11
# assert f_2(2) == 4
# assert f_2(-3) == -11
# assert f_2(1) == 5
# print("Good")
