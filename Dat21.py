import json
from datetime import date
dj={}
sd=list(set([date.fromisoformat(input()) for d in range(int(input()))]))
for i in sd:
    if "days" not in dj: dj["days"]={}
    if i.day not in dj["days"]: dj["days"][i.day]=[]
    dj["days"][i.day].append(i.isoformat())

    if "months" not in dj: dj["months"]={}
    if i.month not in dj["months"]: dj["months"][i.month]=[]
    dj["months"][i.month].append(i.isoformat())

    if "years" not in dj: dj["years"]={}
    if i.year not in dj["years"]: dj["years"][i.year]=[]
    dj["years"][i.year].append(i.isoformat())

print(json.dumps(dj, indent=4))

# # объявляем переменные
# string = "Some test string"
# integer = 211
# array = [1, 2, 3, 4, 5]

# # создаем словарь
# mydict = {"title": string, "code": integer, "data": array}

# # сериализуем его в JSON-структуру, как строку
# x = json.dumps(mydict)

# print(x)