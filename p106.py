def find_keys(**kwargs):
    return sorted([i for i in kwargs if isinstance(kwargs[i], (list,tuple))],key=str.lower)

# def find_keys(**kwargs):
#     s=[]
#     for i in kwargs:
#         if isinstance(kwargs[i], (list,tuple)): s.append(i)
#     return sorted(s,key=str.lower)


assert find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) == ['A', 'b', 't', 'W']
assert find_keys(name='Bruce', surname='Wayne') == []
assert find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) == ['Also', 'marks']



# def count_strings(*args):
#     count_str=0
#     for i in args:
#         if isinstance(i, str): count_str+=1
#     return count_str

# assert count_strings(1, 2, 'hello', [2, 3, 4], True) == 1
# assert count_strings('am', 'world', 'hello', 'is') == 4
# assert count_strings() == 0 
# assert count_strings(True, False) == 0
print('Все проверки пройдены!')