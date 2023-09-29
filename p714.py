# # Напишите определение декоратора memoize  
# from functools import wraps

# def memoize(func):
#     cash={}
#     @wraps(func)
#     def inner(*args,**kwargs):
#         nonlocal cash
#         if args not in cash:
#             cash[args]=func(*args,**kwargs)

#         return cash[args]
    
#     return inner

# # Код ниже не удаляйте, он нужен для проверки   


# @memoize
# def fibonacci(n):
#     """
#     Возвращает n-ое число Фибоначчи
#     """
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# assert fibonacci(50) == 12586269025
# assert fibonacci(60) == 1548008755920
# assert fibonacci(70) == 190392490709135
# assert fibonacci(80) == 23416728348467685
# assert fibonacci(90) == 2880067194370816120
# assert fibonacci(100) == 354224848179261915075
# assert fibonacci.__name__ == 'fibonacci'
# assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
# print('Good')


# # Напишите определение декоратора validate_args
# from functools import wraps

# def validate_args(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         if len(args)>2:
#             return 'Too many arguments'
#         elif len(args)<2:
#             return 'Not enough arguments'
#         elif type(args[0])!=int or type(args[1])!=int:
#             return 'Wrong types'
        
#         return func(*args,**kwargs)
    
#     return inner
# # Код ниже не удаляйте, он нужен для проверки   
# @validate_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y


# assert add_numbers(4, 5) == 9
# assert add_numbers(4) == 'Not enough arguments'
# assert add_numbers() == 'Not enough arguments'
# assert add_numbers('hello') == 'Not enough arguments'
# assert add_numbers(3, 5, 6) == 'Too many arguments'
# assert add_numbers('a', 'b', 'c') == 'Too many arguments'
# assert add_numbers(4.5, 5.1) == 'Wrong types'
# assert add_numbers('hello', 4) == 'Wrong types'
# assert add_numbers(9, 'hello') == 'Wrong types'
# assert add_numbers([1, 3], {}) == 'Wrong types'
# assert add_numbers.__name__ == 'add_numbers'
# assert add_numbers.__doc__.strip() == 'Return sum of x and y'
# print('Good')

# # Напишите определение декоратора add_args  
# from functools import wraps

# def add_args(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         return func('begin',*args,'end',**kwargs)
    
#     return inner
# # Код ниже не удаляйте, он нужен для проверки   
# @add_args
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)


# @add_args
# def find_max_word(*args):
#     """
#     Возвращает слово максимальной длины
#     """
#     return max(args, key=len)


# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
# assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
# assert concatenate.__name__ == 'concatenate'
# assert concatenate.__doc__.strip() == """Возвращает конкатенацию переданных строк"""
# assert find_max_word('my') == 'begin'
# assert find_max_word('my', 'how') == 'begin'
# assert find_max_word('my', 'how', 'maximum') == 'maximum'
# assert find_max_word.__name__ == 'find_max_word'
# assert find_max_word.__doc__.strip() == """Возвращает слово максимальной длины"""