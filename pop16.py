grafclass = {}
listExcecuted = []


def islinkclass(pr, pot):
    if pr == pot or grafclass[pot].count(pr) != 0:
        return True
    else:
        for i in grafclass[pot]:
            if islinkclass(pr, i):
                return True
        return False


for _ in range(int(input())):
    k = input().split()
    grafclass[k[0]] = []
    cl = 2
    while cl < len(k):
        grafclass[k[0]].append(k[cl])
        if k[cl] not in grafclass:
            grafclass[k[cl]] = []
        cl += 1
res = []
for _ in range(int(input())):
    listExcecuted.append(input())
for i in range(len(listExcecuted)):
    for j in grafclass[listExcecuted[i]]:
        for k in range(i):
            if islinkclass(listExcecuted[k], j):
                if listExcecuted[i] not in res:
                    res.append((listExcecuted[i]))
                break
print("\n".join(res))

print(grafclass)
""" Пример решения с форума. Вижу смысл разобраться в этом решении
def checkdup(d):
    return cls[d] is None or any(map(checkdup, cls[d]))

cls = {d: set(b[1:]) for _ in range(int(input())) for d, *b in [input().split()]}

for _ in range(int(input())):
    c = input()
    if checkdup(c):
        print(c)
    cls[c] = None
"""

# grafclass = {}


# def islinkclass(pr, pot):
#     if pr == pot or grafclass[pot].count(pr) != 0:
#         return True
#     else:
#         for i in grafclass[pot]:
#             if islinkclass(pr, i):
#                 return True
#         return False


# for _ in range(int(input())):
#     k = input().split()
#     grafclass[k[0]] = []
#     cl = 2
#     while cl < len(k):
#         grafclass[k[0]].append(k[cl])
#         cl += 1

# for _ in range(int(input())):
#     k = list(input().split())
#     if islinkclass(k[0], k[1]):
#         print("Yes")
#     else:
#         print("No")

# print(grafclass)


# import time


# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))


# # ------------------------------------------------------


# class LoggableList(list, Loggable):
#     def append(self, lst):
#         super().append(lst)
#         self.log(lst)


# a = LoggableList([1, 2])
# print(a)
# a.append(7, 8)
# print(a)
