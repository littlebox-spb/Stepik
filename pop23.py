import itertools


def testsimple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes():
    st = 2
    while True:
        if testsimple(st):
            yield st
        st += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))


# class multifilter:
#     def judge_half(self, n):
#         pos = 0
#         neg = 0
#         for f in self.func:
#             pos += 1 if f(n) else 0
#             neg += 1 if not f(n) else 0
#         return pos > neg

#     def judge_any(self, n):
#         res = False
#         for f in self.func:
#             res = res or f(n)
#         return res

#     def judge_all(self, n):
#         res = True
#         for f in self.func:
#             res = res and f(n)
#         return res

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.func = funcs
#         self.data = iterable
#         self.count = -1
#         self.judge = judge

#     # def __iter__(self):
#     #     for i in self.data:
#     #         if self.judge(self, i):
#     #             yield i

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while True:
#             self.count += 1
#             if self.count < len(self.data):
#                 if self.judge(self, self.data[self.count]):
#                     return self.data[self.count]
#             else:
#                 raise StopIteration


# def mul2(x):
#     return x % 2 == 0


# def mul3(x):
#     return x % 3 == 0


# def mul5(x):
#     return x % 5 == 0


# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]
