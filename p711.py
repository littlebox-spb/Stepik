sa={'Дили':set(), 'Вили':set(), 'Били':set()}
while True:
    s=input()
    if s=='конец': break
    s=s.split(': ')
    sa[s[0]].add(s[1])     
        
for k, v in sorted(sa.items(),key=lambda item: -len(item[1])):
    print(f'Количество уникальных комментаторов у {k} - {len(v)}')

        
# sa={}
# while True:
#     s=input()
#     if s=='конец': break
#     s=s.split(', ')
#     if s[0] in sa:
#         sa[s[0]][0]=sa[s[0]][0]+int(s[1])
#         sa[s[0]][1]+=1
#     else:
#         sa.setdefault(s[0],[]).append(int(s[1]))
#         sa[s[0]].append(1)

# for k, v in sorted(sa.items(),
#                    key=lambda item: (-item[1][0]/item[1][1],item[0])):
#     print(k, v[0]/v[1])


# for key, value in sorted(heroes.items(), 
#                          key=lambda item: item[1]):
#     print(key, value)

# sa={}
# for _ in range(int(input())):
#     s=input().split()
#     sa.setdefault(s[2],[]).append(s[0])
# #    sa[s[2]].append(s[1])

# for _ in range(int(input())):
#     print(*sorted(sa.get(input(), ['Нет данных'])))
    
    
# sa={}
# for _ in range(int(input())):
#     s=input()
#     if s in sa:
#         sa[s]+=1
#     else:
#         sa[s]=1
# sa=sorted(sa.items(),key=lambda item: item[1],reverse=True)
# print(f'{sa[0][0]}, {sa[0][1]}')
# print(f'{sa[len(sa)-1][0]}, {sa[len(sa)-1][1]}')


