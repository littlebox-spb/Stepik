def my_range_gen(*args):
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while args[1] - i != 0:
            yield i
            i += 1
    else:
        if args[2] > 0 and args[0] < args[1]:
            i = args[0]
            while i < args[1]:
                yield i
                i += args[2]
        if args[2] < 0 and args[0] > args[1]:
            i = args[0]
            while i > args[1]:
                yield i
                i += args[2]


for i in my_range_gen(30, 1, -5):
    print(i)
for i in my_range_gen(4, 8, 2):
    print(i)


assert ([i for i in my_range_gen(-5)]) == [i for i in range(-5)]
assert ([i for i in my_range_gen(4, 8)]) == [i for i in range(4, 8)]
assert ([i for i in my_range_gen(4, 8, 2)]) == [i for i in range(4, 8, 2)]
assert ([i for i in my_range_gen(8, 5, -1)]) == [i for i in range(8, 5, -1)]
assert ([i for i in my_range_gen(20, 10, 3)]) == [i for i in range(20, 10, 3)]
assert ([i for i in my_range_gen(30, 1, -5)]) == [i for i in range(30, 1, -5)]
print("Все проверки пройдены")


# def gen_fibonacci_numbers(n):
#     one = 1
#     two = 1
#     for i in range(n):
#         yield one
#         one, two = two, one + two


# for i in gen_fibonacci_numbers(10):
#     print(i)


# n,m = map(int,input().split())
# st=[]
# matrix=[]
# for i in range(n):
#     st.append(input())
#     matrix.append([0]*m)
#     for j in range(m):
#         if st[i][j:j+1]=='*': matrix[i][j]=1
#         else: matrix[i][j]=0
# c=0
# for i in range(n):
#     for j in range(m):
#         s=0
#         if matrix[i][j]==1: s+=1
#         # try: s+=matrix[i-1][j-1]
#         # except: pass
#         if i-1>=0: s+=matrix[i-1][j]
#         # try: s+=matrix[i-1][j+1]
#         # except: pass
#         if j-1>=0: s+=matrix[i][j-1]
#         if j+1<m: s+=matrix[i][j+1]
#         # try: s+=matrix[i+1][j-1]
#         # except: pass
#         if i+1<n: s+=matrix[i+1][j]
#         # try: s+=matrix[i+1][j+1]
#         # except: pass
#         if s ==0: c+=1

# print(matrix,c)
