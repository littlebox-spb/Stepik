# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n 
# и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i!=j:
#             maxrix[i][j] = abs(i-j)

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j],end=' ')
#     print()
# print()


# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. 
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, 
# остальные клетки заполните точками.

# n = input()
# maxrix = [['.'] * 8 for _ in range(8)]

# fpi=int(n[1])-1
# fpj=int(ord(n[0])-ord('a'))

# for i in range(8):
#     for j in range(8):
#         if i==fpi and j==fpj:
#             maxrix[i][j] = 'Q'
#         elif i==fpi or j==fpj or abs(i-fpi)==abs(j-fpj): 
#             maxrix[i][j] = '*'

# for i in range(7,-1, -1):
#     for j in range(8):
#         print(maxrix[i][j],end=' ')
#     print()
# print()

# Латинским квадратом порядка n называется квадратная матрица размером n×n, 
# каждая строка и каждый столбец которой содержат все числа от 1 до n. 
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# f=True
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]
#         if row[j]>n: f=False
        
# for i in range(n):
#     rs=set()
#     for j in range(n):
#         rs.add(maxrix[i][j])
#     if len(rs)!=n:
#         f=False
#         break

# for j in range(n):
#     rs=set()
#     for i in range(n):
#         rs.add(maxrix[i][j])
#     if len(rs)!=n:
#         f=False
#         break

# print('YES' if f else 'NO')


# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# f=True
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]
        
# for i in range(n):
#     for j in range(n):
#         if i!=n-1-j:
#             if maxrix[i][j] != maxrix[n-1-j][n-1-i]:
#                 f=False
#                 break

# print('YES' if f else 'NO')


# На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером n×n 
# заполнив её символами '.' Затем заполните символами '*' среднюю строку и столбец матрицы, 
# главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

# n = int(input())
# maxrix = [['.'] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i==j or i==n-1-j or i==n//2 or j==n//2:
#             maxrix[i][j] = '*'

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j],end=' ')
#     print()
# print()


# Напишите программу, которая транспонирует квадратную матрицу.
# Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# maxrixT = [[0] * n for _ in range(n)]

# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]

# for i in range(n):
#     for j in range(n):
#         maxrixT[j][i]=maxrix[i][j]

# for i in range(n):
#     for j in range(n):
#         print(maxrixT[i][j],end=' ')
#     print()
# print()

# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы (прав+ниж).
# Примечание. Элементы побочной диагонали также учитываются.

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]

# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         maxrix[i][j] = row[j]
# mmax=maxrix[n-1][n-1]
# for i in range(n):
#     for j in range(n):
#         if i >= n - 1 - j:
#             if maxrix[i][j]>mmax:
#                 mmax=maxrix[i][j]

# print(mmax)


# На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список. 
# Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов 
# принадлежат разным подспискам.

# sp=list(input().split())
# n=int(input())
# out=[]

# for i in range(n):
#    out.append([]) 
# i=0   
# for s in sp:
#     out[i].append(s)
#     if i<n-1:
#         i+=1
#     else:
#         i=0
# print (out)