n = int(input())
maxrix = [[0] * n for _ in range(n)]
vch = rch = nch = lch = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        maxrix[i][j] = row[j]

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            vch += maxrix[i][j]
        if i < j and i > n - 1 - j:
            rch += maxrix[i][j]
        if i > j and i < n - 1 - j:
            lch += maxrix[i][j]
        if i > j and i > n - 1 - j:
            nch += maxrix[i][j]


print("Верхняя четверть:", vch)
print("Правая четверть:", rch)
print("Нижняя четверть:", nch)
print("Левая четверть:", lch)

# Верхняя четверть: 5
# Правая четверть: 14
# Нижняя четверть: 5
# Левая четверть: 8


# n=int(input())
# m:int|None=None
# cnt=n//2
# maxrix=[]
# for i in range(n):
#     maxrix=list(map(int,input().split()))
#     if m==None: m=max(maxrix[:i+1])
#     if i<=cnt:
#         m=max(maxrix[:i+1]) if max(maxrix[:i+1])>m else m
#         m=max(maxrix[-i-1:]) if max(maxrix[-i-1:])>m else m
#     else:
#         m=max(maxrix[:i-cnt]) if max(maxrix[:i-cnt])>m else m
#         m=max(maxrix[i-n:]) if max(maxrix[i-n:])>m else m


#     print('******')
#     print(maxrix[:i+1],maxrix[-i-1:],maxrix[:i-cnt],maxrix[i-n:])
#    else:
#        m=max(maxrix[:i-cnt-1]) if max(maxrix[:n-i-1])>m else m
# print(m)


# n=int(input())
# maxrix=[]
# m:int|None=None
# for i in range(n):
#     maxrix=list(map(int,input().split()))
#     if m==None: m=max(maxrix[:i+1])
#     m=max(maxrix[:i+1]) if max(maxrix[:i+1])>m else m
# print(m)

# n=int(input())
# m=int(input())
# maxrix=[[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         maxrix[i][j]=input()

# for i in range(n):
#     for j in range(m):
#         print(maxrix[i][j],end=' ')
#     print()
# print()

# for j in range(m):
#     for i in range(n):
#         print(maxrix[i][j],end=' ')
#     print()
