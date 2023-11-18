grafclass = {}


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
        cl += 1

for _ in range(int(input())):
    k = list(input().split())
    if islinkclass(k[0], k[1]):
        print("Yes")
    else:
        print("No")

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
