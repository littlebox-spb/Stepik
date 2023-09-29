import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(1, 20) if is_prime(i)]
print(primes)





# def decorator(func):
#     # Your decorator code
#     def neg (a,b):
#         if a<0 or b<0: print('YES')
#         s = func(a,b)
#         return s
#     return neg

# # Connect decorator please
# @decorator
# def main(a, b):
#     # Your code here
#     return a+b

# x, y = [int(x) for x in input().split()]
# print(main(x, y))


# from datetime import datetime

# def dec_func(func):
#     def wrapper(arg):
#         t1 = datetime.now()
#         x = func(arg)
#         t2 = datetime.now()
#         print("Time of completing this task:", x, end=" ")
#         return x
#     return wrapper

# @dec_func    
# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res = res * i
#     return res
# fact_100 = factorial(3)
# print(fact_100)

# def decorator_function(func_to_be_called):
#     def wrapper(text):
#         print("Some text before calling function")
#         result = func_to_be_called(text)
#         print("Some text after calling function")
#         return result
        
#     return wrapper

# @decorator_function
# def print_function(text):

#   return "Your text is: " + text

# print(print_function("Hello"))


#print(sum(int(input()) for _ in range(int(input()))))
