# Возведение квадратной матрицы в степень
def matrixpower(a,b):

    def rowtomatrix(r,c,m):
        s=0
        for i in range(len(r)):
            s+=r[i]*m[i][c]
        return s

    matrixC = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            matrixC[i][j]=rowtomatrix(a[i],j,b)
    return matrixC

n=int(input())
matrixA = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    matrixA[i]=[x for x in list(map(int,input().split()))]
m=int(input())
matrixC = [[0 for _ in range(n)] for _ in range(n)]    
matrixC=matrixpower(matrixA,matrixA)
for _ in range(m-2):
    matrixC=matrixpower(matrixC,matrixA)
for i in range(n):
    print(*matrixC[i])



#Умножение матриц
# def rowtomatrix(r,c,m):
#     s=0
#     for i in range(len(r)):
#        s+=r[i]*m[i][c]
#     return s

# n,m=map(int,input().split())
# matrixA = [[None for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     matrixA[i]=[x for x in list(map(int,input().split()))]
# input()
# m,k=map(int,input().split())
# matrixB = [[None for _ in range(k)] for _ in range(m)]
# matrixC = [[0 for _ in range(k)] for _ in range(n)]
# for i in range(m):
#     matrixB[i]=[x for x in list(map(int,input().split()))]

# for i in range(n):
#     for j in range(k):
#         matrixC[i][j]=rowtomatrix(matrixA[i],j,matrixB)

# for i in range(n):
#     print(*matrixC[i])
 
#Сложение матриц

# n,m=map(int,input().split())
# matrixA = [[None for _ in range(m)] for _ in range(n)]
# matrixB = [[None for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     matrixA[i]=[int(x) for x in list(map(int,input().split()))]
# input()
# for i in range(n):
#     matrixB[i]=[int(x) for x in list(map(int,input().split()))]
# for i in range(n):
#     for j in range(m):
#         matrixA[i][j]+=matrixB[i][j]
# for i in range(n):
#     print(*matrixA[i])