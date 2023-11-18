# from pprint import pprint

gnamespace = {"global": []}
gvariable = {}


def get(namespace, var):
    if (namespace in gvariable) and (var in gvariable[namespace]):
        print(namespace)
    else:
        for key, value in gnamespace.items():
            if namespace in value:
                return get(key, var)
        print("None")
    return


# def get(namespace, var):
#     for key, value in gvariable.items():
#         if var in value:
#             if (
#                 (namespace in gvariable)
#                 and (namespace in gnamespace)
#                 and (var in gvariable[namespace])
#             ):
#                 print(namespace)
#                 return
#             else:
#                 for key, value in gnamespace.items():
#                     if namespace in value:
#                         return get(key, var)
#                 print("None")
#                 return
#     print("None")
#     return


def create(namespace, parent):
    if parent in gnamespace:
        gnamespace[parent].append(namespace)
        gnamespace[namespace] = []
        gvariable[namespace] = []


# def create(namespace, parent):
#     global gnamespace
#     global gvariable
#     for key in gnamespace:
#         if key == parent:
#             gnamespace[parent].append(namespace)
#             gnamespace[namespace] = []
#             gvariable[namespace] = []
#             break


def add(namespace, var):
    if namespace in gvariable:
        gvariable[namespace].append(var)
    else:
        gvariable[namespace] = [var]


# def add(namespace, var):
#     global gvariable
#     for key in gvariable:
#         if key == namespace:
#             gvariable[namespace].append(var)
#             return
#     gvariable[namespace] = [var]


test = [
    "create a global",
    "add a a1",
    "add a a2",
    "add a a3",
    "create sub_a a",
    "add sub_a a000",
    "get a a3",
    "get a a2",
    "get a a1",
    "get a b0",
    "get sub_a a1",
    "get sub_a a",
    "get sub_a a000",
    "get global a1",
    "get global a",
]


# for _ in range(int(input())):
for i in range(15):
    # func, namespace, var = input().split()
    func, namespace, var = test[i].split()
    exec(f"{func}('{namespace}','{var}')")

    # pprint(gnamespace)
"""
a
a
a
None
a
None
sub_a
None
None
"""
