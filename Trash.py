n,m = map(int,input().split())
st=[]
matrix=[]
for i in range(n):
    st.append(input())
    matrix.append([0]*m)
    for j in range(m):
        if st[i][j:j+1]=='*': matrix[i][j]=1
        else: matrix[i][j]=0
c=0
for i in range(n):
    for j in range(m):
        s=0
        if matrix[i][j]==1: s+=1
        # try: s+=matrix[i-1][j-1]
        # except: pass
        if i-1>=0: s+=matrix[i-1][j]
        # try: s+=matrix[i-1][j+1]
        # except: pass
        if j-1>=0: s+=matrix[i][j-1]
        if j+1<m: s+=matrix[i][j+1]
        # try: s+=matrix[i+1][j-1]
        # except: pass
        if i+1<n: s+=matrix[i+1][j]
        # try: s+=matrix[i+1][j+1]
        # except: pass
        if s ==0: c+=1

print(matrix,c)