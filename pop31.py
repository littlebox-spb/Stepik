s1, s2, pos = [input() for i in range(2)] + [0]
if s2 in s1:
    for c in range(len(s1)):
        if s1.find(s2, pos) == -1:
            break
        else:
            pos = 1 + s1.find(s2, pos)
    else:
        c += 1
    print(c)
else:
    print(0)

# Не мое решение
s = input()
t = input()

print(sum(1 for i in range(len(s)) if s.startswith(t, i)))

# s, a, b = input(), input(), input()
# c = 0
# while True:
#     if c > 1000:
#         print("Impossible")
#         break
#     else:
#         if s.find(a) == -1:
#             print(c)
#             break
#         else:
#             s = s.replace(a, b)
#     c += 1

# Не мое решение
# s, a, b, i = [input() for i in range(3)] + [0]
# while a in s:
#     if a in b:
#         i = "Impossible"
#         break
#     s, i = s.replace(a, b), i + 1
# print(i)
