st=input()+' запретил'+' букву'
s=list(sorted(set(i for i in st)))[1:]

for i in s:
    print(word.strip(),i)
    word=word.replace(i,'')
    word=word.replace('  ',' ')
    

# sp=list([input() for i in range(int(input()))])
# cs='anton'
# cnt=1
# out=[]
# for i in sp:
#     cc=''
#     k=0
#     for j in i:
#         if j == cs[k]:
#             k+=1
#             cc+=j
#             if k>4: break
#     if cc==cs:
#         out.append(cnt)
#     cnt+=1
# print(*out)

# sp=list([i for i in input()])

# c=0
# cm=0
# for i in sp:
#     if i=='Р':
#         c+=1
#     else:
#         if c>0:
#             if c>cm and c>0:
#                 cm=c
#             c=0
# print(cm if cm>c else c)

# t = input()
# r = input()
# if t == r:
#     print("ничья")
# else:
#     match t:
#         case "камень":
#             if r in ("бумага","Спок"):
#                 print("Руслан")
#             else:
#                 print("Тимур")
#         case "бумага":
#             if r in ("ножницы","ящерица"):
#                 print("Руслан")
#             else:
#                 print("Тимур")
#         case "ножницы":
#             if r in ("камень","Спок"):
#                 print("Руслан")
#             else:
#                 print("Тимур")
#         case "ящерица":
#             if r in ("камень","ножницы"):
#                 print("Руслан")
#             else:
#                 print("Тимур")
#         case "Спок":
#             if r in ("ящерица","бумага"):
#                 print("Руслан")
#             else:
#                 print("Тимур")


# sn = [int(input()) for i in range(int(input()))]
# pr = int(input())
# for i in range(len(sn)):
#     if sn[i] == 0:
#         continue
#     if pr % sn[i] == 0 and pr // sn[i] in sn:
#         if pr == sn[i] ** 2 and sn.count(sn[i]) == 1:
#             continue
#         print("ДА")
#         break
# else:
#     print("НЕТ")


# n = list(map(int, input().split()))
# out = []
# out.append(n[-1])
# n.pop(-1)
# for i in range(len(n)):
#     out.append(n[i])
# print(*out)

# n = list(map(int, input().split()))
# c = 0
# for i in range(1, len(n), 2):
#     c = n[i]
#     n[i] = n[i - 1]
#     n[i - 1] = c
# print(*n)


# n = list(map(int, input().split()))
# c = 0
# for i in range(1, len(n)):
#     if n[i] > n[i - 1]:
#         c += 1
# print(c)


# n = int(input())

# p1 = p2 = p3 = p4 = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x == 0 or y == 0:
#         continue
#     elif x > 0 and y > 0:
#         p1 += 1
#     elif x > 0 and y < 0:
#         p4 += 1
#     elif x < 0 and y > 0:
#         p2 += 1
#     else:
#         p3 += 1
# print("Первая четверть:", p1)
# print("Вторая четверть:", p2)
# print("Третья четверть:", p3)
# print("Четвертая четверть:", p4)
