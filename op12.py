objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

tmp=set()
for obj in objects:
    tmp.add(id(obj))

print(len(tmp))

print(len(set(map(id,objects))))


# x = [1, 2, 3]
# y = x
# y.append(4)

# s = "123"
# t = s
# t = t + "4"

# print(str(x) + " " + s)