
n=4
m=5
ns=[1, 4, 6, 2]
ms=[5, 1, 5, 7, 9]
'''

n=int(input())
ns=list(input().split())
m=int(input())
ms=list(input().split())
'''

result=ns+ms
k=0
while k<2:
    if k==0: 
        result=ns
        l=n-1
    else: 
        result=ms
        l=m-1
    j=0
    f=True
    while j<l:
        i=0
        while i<l:
            if int(result[i])>int(result[i+1]): 
                z=result[i]
                result[i]=result[i+1]
                result[i+1]=z
                f=False
            i+=1
        j+=1
        if f: i=j=n+m
    if k==0: 
        ns=result
    else: 
        ms=result
    k+=1
i=j=0
k=0
while i<len(ns)!=0:
    j=0
    f=True
    while j<len(ms) and f:
        print(i,'->',*ns,'\n',j,'->',*ms)
        if abs(int(ns[i])-int(ms[j]))<=1: 
            k+=1
            del ns[i]
            del ms[j]
            f=False
            i=j=0
        j+=1
    if f: i+=1
print(k)        

