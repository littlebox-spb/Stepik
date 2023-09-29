n = int(input())
maxrix = [[0] * n for _ in range(n)]
f=True
gs=vs=cs=0
db=set()
rs=set()
for i in range(n):
    row = list(map(int, input().split()))
    rs.add(sum(row))
    for j in range(n):
        maxrix[i][j] = row[j]
        db.add(row[j])
        if row[j]==0: f=False

for i in range(n):
    for j in range(n):
        cs+=maxrix[j][i]
        if i==j: gs+=maxrix[i][j]
        if i==n-j-1: vs+=maxrix[i][j]            
    rs.add(cs)
    cs=0
rs.add(gs)
rs.add(vs)
if len(rs)!=1: f=False
if n*n!=len(db): f=False
print('YES' if f else 'NO')


# def sign(x:int,y:int,ch:str):
#     maxrix[8-x][y]=ch

# n = input()
# maxrix = [[' . '] * 8 for _ in range(8)]
# rw=int(n[1])
# cl=ord(n[0])-97
# sign(rw,cl,'N ')

# if rw+2<=8 and cl-1>=0: sign(rw+2,cl-1,'* ')
# if rw+2<=8 and cl+1<8: sign(rw+2,cl+1,'* ')
# if rw-2>0 and cl-1>=0: sign(rw-2,cl-1,'* ')
# if rw-2>0 and cl+1<8: sign(rw-2,cl+1,'* ')
# if cl+2<8 and rw-1>0: sign(rw-1,cl+2,'* ')
# if cl+2<8 and rw+1<=8: sign(rw+1,cl+2,'* ')
# if cl-2>=0 and rw-1>0: sign(rw-1,cl-2,'* ')
# if cl-2>=0 and rw+1<=8: sign(rw+1,cl-2,'* ')

# for i in range(8):
#     for j in range(8):
#         print(maxrix[i][j].rjust(3), end=" ")
#     print()


# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# maxrix90 = [[0] * n for _ in range(n)]
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]

# for i in range(n):
#     for j in range(n):
#         maxrix90[j][n-i-1]=maxrix[i][j]

# for i in range(n):
#     for j in range(n):
#         print(maxrix90[i][j], end=" ")
#     print()


# n = int(input())
# maxrix = {}
# for i in range(n):
#     row = input()
#     maxrix[i]=[row]
# for i in range(n-1,-1,-1):
#     print(*maxrix[i])


# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]

# for i in range(n):
#     for j in range(n):
#         if i==j:
#             tmp=maxrix[i][j]
#             maxrix[i][j]=maxrix[n-j-1][i]
#             maxrix[n-j-1][i]=tmp

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()



# n = int(input())
# f=True
# maxrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]

# for i in range(n):
#     for j in range(n):
#         if i!=j:
#             if maxrix[i][j]!=maxrix[j][i]:
#                 f=False
# print('YES' if f else 'NO')


# n = int(input())
# m = int(input())
# maxrix = [[0] * m for _ in range(n)]
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(m):
#         maxrix[i][j] = row[j]
# cl1, cl2 = map(int, input().split())

# for i in range(n):
#     for j in range(m):
#         if j == cl1:
#             s1 = maxrix[i][j]
#         if j == cl2:
#             s2 = maxrix[i][j]
#     maxrix[i][cl1] = s2
#     maxrix[i][cl2] = s1

# for i in range(n):
#     for j in range(m):
#         print(maxrix[i][j], end=" ")
#     print()

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
