class Person:
    def tell_about_yourself(self):
        print("Я Человек")


class Doctor(Person):
    def tell_about_yourself(self):
        super(Surgeon, self).tell_about_yourself()
        print("Я Доктор")


class Surgeon(Doctor):
    def tell_about_yourself(self):
        print("Я Хирург")


d = Doctor()
d.tell_about_yourself()

# import colorsys

# print(colorsys.rgb_to_hsv(0.3, 0.4, 0.2))

# (0.25, 0.5, 0.4)

# for i in input().replace(" ", "").replace("'", "").split(","):
#     if "+" in i:
#         print(f"({i})")
#     else:
#         print(i)


# s = input().replace(" ", "").replace("'", "").split(",")
# print(s)
# st = 0
# for i in range(len(s)):
#     if s[i] == ",":
#         print(s[st:i])
#         st = i + 1
# print(s[st : len(s)])

# s = "H9el546l=o* W7o91r5++l%98d"
# m = ""
# for i in s:
#     if i.isalpha() or i == " ":
#         m += i
# print(m)


# def rev(s):
#     if len(s) == 0:
#         return
#     rev(s[1:])
#     print(s[0:1])


# rev(input())

# def slist(l):
#     if len(l) == 1:
#         return int(l[0])
#     else:
#         e = l.pop()
#         return int(e) + slist(l)


# print(slist(input().replace(",", " ")[1:-1].split()))


# d = {}
# while True:
#     try:
#         s = input().split()
#     except EOFError:
#         break
#     if s[0] not in d:
#         d[s[0]] = {}
#     if s[1] not in d[s[0]]:
#         d[s[0]][s[1]] = 0
#     d[s[0]][s[1]] += int(s[2])
# print(d)


# points = [(12, 55), (880, 123), (64, 64), (190, 1024), (77, 33), (42, 11), (0, 90)]

# p = list(map(int, input().split()))
# kan = 0
# otk = ((points[0][0] - p[0]) ** 2 + (points[0][1] - p[1]) ** 2) ** 0.5
# for k in range(1, len(points)):
#     tok = ((points[k][0] - p[0]) ** 2 + (points[k][1] - p[1]) ** 2) ** 0.5
#     if tok < otk:
#         kan = k
#         otk = tok
# print(*points[kan])

# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a)
# print(b)
# print(c)
# print(d)


# evens = [i**2 for i in range(10) if i ** 2 % 2 == 0]

# print(evens)

# for x in range(0, -5, -1):
#     if x == -1:
#         continue
#     elif x == -3:
#         break
#     print(x)

# n = input()
# c1, c2 = list(n[0:3]), list(n[3:6])
# s1, s2 = 0, 0
# for i in range(3):
#     s1 += int(c1[i])
#     s2 += int(c2[i])
# print("Счастливый билет" if s1 == s2 else "Несчастливый билет")


# class A:
#     val = 1

#     def foo(self):
#         A.val += 2

#     def bar(self):
#         self.val += 1


# a = A()
# b = A()

# a.bar()
# a.foo()

# c = A()

# print(a.val)
# print(b.val)
# print(c.val)

# start = 12
# end = 21


# def pr(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# for j in range(start, end + 1):
#     if pr(j):
#         print(f" {j}")


# str = "hello_world!"
# big = ord(str[0])
# for i in range(1, len(str)):
#     if big < ord(str[i]):
#         big = ord(str[i])

# print(chr(big))


# k=3
# for i in range(10):
#     k+=1
#     if (i>5):
#         k+=1
# print(k)


"""
from contextlib import contextmanager;


@contextmanager;
def my_context_manager():;
    print("Начало контекстного менеджера ...");
    yield "Ух ты как круто!";
    print("Конец контекстного менеджера...");


with my_context_manager() as phrase:;
    print(phrase);
"""
