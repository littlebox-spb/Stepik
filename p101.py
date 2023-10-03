def my_range_gen(*args):
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while args[1] - i != 0:
            yield i
            i += 1
    else:
        if args[2] > 0 and args[0] < args[1]:
            i = args[0]
            while i < args[1]:
                yield i
                i += args[2]
        if args[2] < 0 and args[0] > args[1]:
            i = args[0]
            while i > args[1]:
                yield i
                i += args[2]


for i in my_range_gen(30, 1, -5):
    print(i)
for i in my_range_gen(4, 8, 2):
    print(i)


week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days = ((d, week[(d + 4) % 7]) for d in range(1, 78))
for _ in range(77):
    print(next(days))
