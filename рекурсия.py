# def my_pow(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * my_pow(x, y - 1)


# x, y = map(int, input().split())
# print(my_pow(x, y))

# N = 7


# def fib_rec(N, f=[1, 1]):
#     if N > 2:
#         f.append(f[-1] + f[-2])
#         fib_rec(N - 1, f)
#     return f


# print(*fib_rec(N))

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ["True", [-2, -1]]], 7.89]

"""
Чужое решение

def get_line_list(d, a=[]):
    [get_line_list(f, a) if type(f) == list else a.append(f) for f in d]
    return a
"""


# здесь продолжайте программу
def get_line_list(d, a=[]):
    if len(d) == 0:
        return a
    else:
        if type(d[0]) == list:
            get_line_list(d[0])
            a.extend(d.pop(0))
        else:
            a.append(d.pop(0))
        get_line_list(d)
        return a


print(get_line_list(d))
