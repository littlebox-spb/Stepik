# Вариант проверку прошел


def multiply_set(nlst):
    return nlst[0] * nlst[1] * nlst[2]


single = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
]
n = int(input())
result = []
max_num = 0

for i1 in single:
    for i2 in single:
        for i3 in single:
            number_set = [i1, i2, i3]
            if multiply_set(number_set) <= n:
                result.append(number_set)
            else:
                if max_num == 0:
                    max_num = i3
                break
        if i2 > max_num:
            break
    if i1 > max_num:
        break
print(result)


# Вариант рабочий, но не прошел проверку
def multiply_set(nlst):
    return nlst[0] * nlst[1] * nlst[2]


def shift_set(nlst):
    global result
    result.add((nlst[1], nlst[0], nlst[2]))
    result.add((nlst[1], nlst[2], nlst[0]))
    result.add((nlst[2], nlst[1], nlst[0]))
    result.add((nlst[2], nlst[0], nlst[1]))
    result.add((nlst[0], nlst[1], nlst[2]))
    result.add((nlst[0], nlst[2], nlst[1]))


single = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
]
n = int(input())
result = set()

for i1 in single:
    for i2 in single:
        for i3 in single:
            number_set = (i1, i2, i3)
            if multiply_set(number_set) <= n:
                shift_set(number_set)
            else:
                max_num = i3
                break
        if i2 > max_num:
            break
    if i1 > max_num:
        break
out = []
for i in result:
    out.append(list(i))
print(out)
