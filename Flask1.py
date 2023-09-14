class Elevator:

    def __init__(self,et=5,cur=3):
        self.et=et
        self.cur=cur

    def up(self):
        if self.cur+1>self.et: print('Лифт не может подняться выше')
        else: 
            self.cur+=1
            print(f'Лифт поднимается на {self.cur} этаж')

    def down(self):        
        if self.cur-1<1: print('Лифт не может опуститься ниже')
        else: 
            self.cur-=1
            print(f'Лифт опускается на {self.cur} этаж')
        



# def detect_lucky(n):
#     s=[0]*2
#     for i in range(2):
#         for j in range(3):
#             s[i]+=n%10
#             n//=10
#     return s[0]==s[1]


# print(detect_lucky(985778))

# def solution():
#     x = input().split()
#     # ...
#     res=[]
#     f=True
#     for i in x:
#         if i.isalpha(): res.append(i)
#         elif not i.isalpha() and len(res)==1: res.pop()
#         if len(res)==2: 
#             print (*res)
#             res=[]
#             f=False
#     if f: print ('Мало слов!')

# solution()