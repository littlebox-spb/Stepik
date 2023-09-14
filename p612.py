print(["7" * i for i in range(1, 7)])


# s = set()
# for i in input():
#     if i not in s:
#         s.add(i)
#         print(i, end="")


# s = set()
# o = set()
# for z in input():
#     if z.isdigit():
#         if z not in s:
#             s.add(z)
#         else:
#             o.add(z)
# if len(o) != 0:
#     print(*list(sorted(o)))
# else:
#     print("NO")


# print(*sorted(set(input().split()) - set(input().split()), key=int))


# s = set()
# l = 0
# for i in input().split(","):
#     s.add(i.lower())
#     if l == len(s):
#         print("ДА")
#     else:
#         print("НЕТ")
#         l = len(s)


# s = []
# for i in range(int(input())):
#     s.append(input().split())
# p = set(s[0])
# for i in range(1, len(s)):
#     p |= set(s[i])

# print(len(p))
