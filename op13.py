def countCombine(n,k):
    if k==0:
        return 1
    if k>n:
        return 0
    return countCombine(n-1,k)+countCombine(n-1,k-1)

n,k=map(int,input().split())
print (countCombine(n,k))



# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res

# print(s(b=31, 0))


# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     return x+5-x%5


# print (closest_mod_5(4))
# print (closest_mod_5(5))
# print (closest_mod_5(6))
# print (closest_mod_5(7))


# print(7,7//5,7%5, 7+(5-7%5))


# a = []

# def foo(arg1, arg2):
#   a.append("foo")

# foo(a.append("arg1"), a.append("arg2"))

# print(a)