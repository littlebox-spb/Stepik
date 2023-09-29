def create_actor(name='Райан',surname='Рейнольдс',age=46,**kwargs):
    dact={}
    dact['name']=name
    dact['surname']=surname
    dact['age']=age
    dact.update(kwargs)
    return dact

print(create_actor())

# def info_kwargs(**kwargs):
#     for i in sorted(kwargs):
#         print(f'{i} = {kwargs[i]}')

# info_kwargs(first_name="John", last_name="Doe", age=33) 

# def print_goods(*args):
#     sh=0
#     for i in args:
#         if type(i) is str and i.isalpha():
#             sh+=1
#             print(f'{sh}. {i}')
#     if sh==0:
#         print('Нет товаров')


# print_goods('apple', 'banana', 'orange')
# # Программа должна вывести следующее:
# # 1. apple 
# # 2. banana
# # 3. orange

# print_goods(1, True, 'Грушечка', '', 'Pineapple') 
# # Программа должна вывести следующее:
# # 1. Грушечка
# # 2. Pineapple
# print_goods([], {}, 1, 2) 
# # Программа должна вывести следующее:
# # Нет товаров
