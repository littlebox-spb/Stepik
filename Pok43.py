# ob:list=[[],]
# s:list=input().split()

# for cs in range(1,len(s)+1):
#     oc=0
#     for oc in range(len(s)-cs+1):
#         v=[]
#         for i in range(cs):
#             if oc < len(s): v.append(s[oc+i])
#         ob.append(v)
# print (ob)

# def chunked(s:list,n:int):
#     so:list=[]
#     vs:list=[]
#     i=0
#     while i<len(s):
#         for j in range(n):
#             vs.append(s[i])
#             i+=1 
#             if i==len(s): break
#         so.append(vs)
#         vs=[]
#     print(so)



# s:list=input().split()
# n:int=int(input())
# chunked(s,n)


# # s:list=input().split()
# # so:list=[]
# # vs:list=[]
# # for i in s:
# #     if not vs: 
# #         vs.append(i)
# #         continue
# #     if i in vs : 
# #         vs.append(i)
# #     else:
# #         so.append(vs)
# #         vs=[]
# #         vs.append(i)
# # if vs: so.append(vs)
# # print(so)


# # def pascal(row):
# #     tp=[]
# #     for i in range(row+1):
# #         if len(tp)<1:
# #             tp.append([1])
# #         elif len(tp)<2:
# #             tp.append([1,1])
# #         else:
# #             vs=[1]
# #             for j in range(len(tp[i-1])-1):
# #                 vs.extend([tp[i-1][j]+tp[i-1][j+1]])
# #             vs.extend([1])                
# #             tp.append(vs)
# #     return tp[row]


# # print(pascal(int(input())))



