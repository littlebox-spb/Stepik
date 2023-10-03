def gen_fibonacci_numbers(n):
    one = 1
    two = 1
    for i in range(n):
        yield one
        one, two = two, one + two


for i in gen_fibonacci_numbers(10):
    print(i)
