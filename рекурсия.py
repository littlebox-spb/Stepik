def my_pow(x, y):
    if y == 0:
        return 1
    else:
        return x * my_pow(x, y - 1)


x, y = map(int, input().split())
print(my_pow(x, y))
