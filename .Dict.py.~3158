sp=list(int(i) for i in input().split())
d={sp[-2]:sp[-1]}
i=len(sp)-3
res={}
while i >= 0:
    if len(res)==0:
        res[sp[i]]=d
    else:
        d=dict(res)
        res={}
        res[sp[i]]=d
    i-=1

print(res)




