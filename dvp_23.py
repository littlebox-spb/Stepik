import datetime
import time

dataIn = []
dataPre = []
dataResult = []
fmt = "%M:%S"
for _ in range(int(input())):
    dataIn = input().split()
    dataPre.append([time.strptime(dataIn[0], fmt), int(dataIn[1])])
sl = int(input())
for d in dataPre:
    if d[1] == sl:
        dataResult.append(d[0].tm_min * 60 + d[0].tm_sec)
if dataResult:
    dataResult.sort()
    if len(dataResult) % 2 == 0:
        td = (
            int(
                (
                    dataResult[len(dataResult) // 2]
                    + dataResult[(len(dataResult) // 2) - 1]
                )
                / 2
            )
            * 2
        )
    else:
        td = dataResult[len(dataResult) // 2] * 2
    hh = int(td / 60 / 60)
    mm = int(td / 60) - hh * 60
    ss = int(td) - mm * 60 - hh * 60 * 60
    print(datetime.time(hour=hh, minute=mm, second=ss))
else:
    print("Мало данных")

# import random
# import time

# delay = (1, 2, 3, 4)

# sp = []


# def timer(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         key = f"{func.__name__}{args} ->"
#         value = int(time.time() - start)
#         if not sp:
#             sp.append(
#                 {
#                     f"{func.__name__}{args} ->": value,
#                 },
#             )
#         else:
#             for i in sp:
#                 if key in i:
#                     if i[key] > value:
#                         i[key] = value
#                     break
#             else:
#                 sp.append(
#                     {
#                         f"{func.__name__}{args} ->": value,
#                     },
#                 )
#         with open("result_time.txt", "w") as f:
#             for i in sp:
#                 for key, value in i.items():
#                     f.write(f"{key} {value}\n")
#         return result

#     return inner


# @timer
# def foo(x, y):
#     time.sleep(1)
#     return x * y


# @timer
# def func(x, y):
#     time.sleep(random.uniform(2, 4))
#     return x * y


# foo(30, 40)
# func(3, 4)
# func(1, 2)
# func(3, 4)

# print(*sp)
