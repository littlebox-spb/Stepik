n = int(input())
m = int(input())
maxrix = [[0] * m for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        maxrix[i][j] = row[j]
cl1, cl2 = map(int, input().split())

for i in range(n):
    for j in range(m):
        if j == cl1:
            s1 = maxrix[i][j]
        if j == cl2:
            s2 = maxrix[i][j]
    maxrix[i][cl1] = s2
    maxrix[i][cl2] = s1

for i in range(n):
    for j in range(m):
        print(maxrix[i][j], end=" ")
    print()

# n = int(input())
# m = int(input())
# maxrix = [[0] * m for _ in range(n)]
# rw = col = 0
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(m):
#         maxrix[i][j] = row[j]
#         if i == 0 and j == 0:
#             km = row[j]
#         if km < row[j]:
#             km = row[j]
#             rw = i
#             col = j
# print(rw, col)

# n = int(input())
# m = int(input())
# maxrix = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         maxrix[i][j] = i * j

# for i in range(n):
#     for j in range(m):
#         print(str(maxrix[i][j]).ljust(3), end=" ")
#     print()
