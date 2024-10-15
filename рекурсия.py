# def my_pow(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * my_pow(x, y - 1)


# x, y = map(int, input().split())
# print(my_pow(x, y))

N = 7


def fib_rec(N, f=[1, 1]):
    if N > 2:
        f.append(f[-1] + f[-2])
        fib_rec(N - 1, f)
    return f


print(*fib_rec(N))
