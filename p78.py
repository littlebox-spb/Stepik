def quick_sort(s):
    A=[]
    B=[]
    D=[]
    if len(s)<=1: return s
    mid=s[0]
    for i in range(len(s)):
        if s[i]<mid:
            A.append(s[i])
        elif s[i]==mid:
            D.append(s[i])
        else:
            B.append(s[i])
    return quick_sort(A)+D+quick_sort(B)

print (quick_sort([19, 4, 5, 17, 1]))
assert quick_sort([19, 4, 5, 17, 1]) == [1, 4, 5, 17, 19]

print (quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))
assert quick_sort([16, 19, 2, 12, 20, 15, 20, 15]) == [2, 12, 15, 15, 16, 19, 20, 20]

print (quick_sort([12, 13, 13, 1, 13, 3, 19, 8, 4]))
assert quick_sort([12, 13, 13, 1, 13, 3, 19, 8, 4]) == [1, 3, 4, 8, 12, 13, 13, 13, 19]

# # функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     n = m = k = 0
#     C = [0] * (len(a) + len(b))
#     while n < len(a) and m < len(b):
#         if a[n] <= b[m]:
#             C[k] = a[n]
#             n += 1
#         else:
#             C[k] = b[m]
#             m += 1
#         k += 1
#     while n < len(a):
#         C[k] = a[n]
#         n += 1
#         k += 1
#     while m < len(b):
#         C[k] = b[m]
#         m += 1
#         k += 1
#     return C


# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     return merge_two_list(merge_sort(s[: len(s) // 2]), merge_sort(s[len(s) // 2 :]))


# assert merge_sort([11, 15, 19, 20, 20, 6, 4, 16, 8]) == [4, 6, 8, 11, 15, 16, 19, 20, 20]
# n = int(input())
# s = list(map(int, input().split()))
# print(*quick_sort(s))

# def flatten_dict(idict: dict, odict=None, parentkey=None):
#     if odict == None:
#         odict = {}
#     for i in idict:
#         nk = i if parentkey == None else parentkey + "_" + i
#         if type(idict[i]) is dict:
#             flatten_dict(idict[i], odict, nk)
#         else:
#             odict[nk] = idict[i]
#     return odict


# nested = {"Germany": {"berlin": 7}, "Europe": {"italy": {"Rome": 3}}, "USA": {"washington": 1, "New York": 4}}
# assert flatten_dict(nested) == {"Germany_berlin": 7, "Europe_italy_Rome": 3, "USA_washington": 1, "USA_New York": 4}

# nested = {"Q": {"w": {"E": {"r": {"T": {"y": 123}}}}}}
# assert flatten_dict(nested) == {"Q_w_E_r_T_y": 123}


# not_nested = {"a": 100, "b": 200}
# assert flatten_dict(not_nested) == {"a": 100, "b": 200}

# def flatten(sp: list, ps=None):
#     if ps == None:
#         ps = []
#     while len(sp) > 0:
#         if type(sp[0]) is list:
#             flatten(sp[0], ps)
#         else:
#             ps.append(sp[0])
#         sp.pop(0)
#     return ps


# assert flatten([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
# assert flatten([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
# assert flatten([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
# print("Все проверки пройдены!")

print("Все проверки пройдены!")
