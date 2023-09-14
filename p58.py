n, m = map(int, input().split())
s=[]
count=0

for i in range(n):
    s.append([0]*m)
    st=input().replace('S','1')
    st=st.replace('.','0')
    for j in range(m):
        s[i][j]=int(st[j])

tcol=[]
trow=[]

for i in range(n):
    if sum(s[i])==0: tcol.append(i)

for j in range(m):
    srow=0
    for i in range(n):
        srow+= s[i][j]
    if srow==0: trow.append(j)
 
for i in tcol:
    for j in range(m):
        if s[i][j]==0:
            s[i][j]=1
            count+=1        

for j in trow:
    for i in range(n):
        if s[i][j]==0:
            s[i][j]=1
            count+=1        

print(count)    







# n, m = map(int, input().split())

# f = True
# for i in range(n):
#     s = input()
#     if s.find("C") == -1 and s.find("M") == -1 and s.find("Y") == -1:
#         f = f and True
#     else:
#         f = f and False
# print("#Black&White" if f else "#Color")


# sp = []
# a = 0
# for i in range(n):
#     sp.append([0] * m)
#     if i % 2 == 0:
#         j = 0
#         while j < m:
#             sp[i][j] = a
#             j += 1
#             a += 1
#     else:
#         j = m - 1
#         while j >= 0:
#             sp[i][j] = a
#             j -= 1
#             a += 1
# for i in range(n):
#     for j in range(m):
#         print(sp[i][j], " ", end="")
#     print()
