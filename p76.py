def create_matrix(size: int=3, up_fill: int = 0, down_fill: int = 0):
    maxrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i==j: maxrix[i][i]=i+1
            elif i<j: maxrix[i][j]=up_fill
            elif i>j: maxrix[i][j]=down_fill
            
    return maxrix


assert create_matrix() == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
assert create_matrix(4) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]

assert create_matrix(up_fill=7) == [[1, 7, 7],
                             [0, 2, 7],
                             [0, 0, 3]]

assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
                                          [9, 2, 7],
                                          [9, 9, 3]]


assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
                                                  [9, 2, 7, 7],
                                                  [9, 9, 3, 7],
                                                  [9, 9, 9, 4]]
print('Проверки пройдены')



# def make_header(text: str, tag: str = '1'):
#     return f'<h{tag}>{text}</h{tag}>'

# assert make_header('Нет') == '<h1>Нет</h1>'
# assert make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
# assert make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
# assert make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'

# def replace(text: str, old: str, new: str = ''):
#     if text.find(old) == -1: return text
#     else: 
#         while text.find(old)!=-1:
#             s=''
#             st=text.find(old)+len(old)
#             s=text[:text.find(old)]
#             s+=new*len(old)
#             s+=text[st:]
#             text=s
#         return s
    
    

# print(replace('Нет', 'т'))# => 'Не'
# print(replace('Bella Ciao', 'a'))# => 'Bell Cio'
# print(replace('nobody; i myself farewell analysis', 'l', 'z'))# => 'nobody; i mysezf farewezz anazysis'
# print(replace('commend me to my kind lord meaning', 'M', 'w'))# => 'commend me to my kind lord meaning'    