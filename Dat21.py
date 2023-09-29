n = int(input())
f = True
sp = []
for i in range(n):
    sp.append(list(map(int, input().split())))
while f:
    for i in range(len(sp)):
        for j in range(i, len(sp)):
            if sp[i][0] > sp[j][0] or (sp[i][0] == sp[j][0] and sp[i][1] > sp[j][1]):
                sp[i], sp[j] = sp[j], sp[i]
    f = False
    for i in range(len(sp) - 1):
        if (sp[i][0] <= sp[i+1][0] <= sp[i][1]) and (sp[i][0] <= sp[i+1][1] <= sp[i][1]):
            f = True
            sp.pop(i+1)
            break
        if (sp[i+1][0] == sp[i][1]+1) or ((sp[i][0] <= sp[i+1][0] <= sp[i][1]) and sp[i][1]<sp[i+1][1]):
            f = True
            sp.append([sp[i][0], sp[i+1][1]])
            sp.pop(i+1)
            sp.pop(i)
            break
print(sp)


# from datetime import date


# def is_vis(d):
#     return (d % 4 == 0 and d % 100 != 0) or (d % 400 == 0 and d % 100 == 0)


# sp = []
# dp = date.fromisoformat(input())
# sd = list([date.fromisoformat(input()) for d in range(int(input()))])
# for i in sd:
#     if i.day == dp.day and i.month == dp.month:
#         sp.append(i)
#     if dp.day == 28 and dp.month == 2 and i.day == 29 and i.month == 2:
#         if is_vis(i.year) and not is_vis(dp.year):
#             sp.append(i)

# if len(sp) == 0:
#     print("Поздравлять некого")
# else:
#     for i in sp:
#         print(i)

# import calendar

# cal = calendar.Calendar()
# wyear = int(input())
# wc = 0
# for i in cal.yeardayscalendar(wyear):
#     for j in i:
#         for k in j:
#             if k[0] != 0:
#                 wc += 1
# print(wc)


# from datetime import date
# import calendar
# d = date.fromisoformat(input())
# cal= calendar.Calendar()
# print(max(cal.itermonthdays(d.year, d.month)))

# import datetime
# sd=list(input().split())
# start=datetime.datetime.strptime(sd[0],'%Y-%m-%d')
# end=datetime.datetime.strptime(sd[1],'%Y-%m-%d')
# for i in range(int(input())):
#     sd=list(input().split())
#     kstart=datetime.datetime.strptime(sd[0],'%Y-%m-%d')
#     kend=datetime.datetime.strptime(sd[1],'%Y-%m-%d')
#     if kstart>=start and kstart<=end or kend>=start and kend<=end or kstart<start and kend>end:
#         print(kstart.date(),kend.date())

# #Решение автора
# from datetime import date

# filter_date_from, filter_date_to = [date.fromisoformat(d) for d in input().split()]

# for _ in range(int(input())):
#     raw = input()
#     date_from, date_to = [date.fromisoformat(d) for d in raw.split()]
#     if (
#         filter_date_from <= date_from <= filter_date_to
#         or filter_date_from <= date_to <= filter_date_to
#         or date_from <= filter_date_from <= date_to
#         or date_from <= filter_date_to <= date_to
#     ):
#         print(raw)


# import json
# from datetime import date
# dj={}
# sd=list(set([date.fromisoformat(input()) for d in range(int(input()))]))
# for i in sd:
#     if "days" not in dj: dj["days"]={}
#     if i.day not in dj["days"]: dj["days"][i.day]=[]
#     dj["days"][i.day].append(i.isoformat())

#     if "months" not in dj: dj["months"]={}
#     if i.month not in dj["months"]: dj["months"][i.month]=[]
#     dj["months"][i.month].append(i.isoformat())

#     if "years" not in dj: dj["years"]={}
#     if i.year not in dj["years"]: dj["years"][i.year]=[]
#     dj["years"][i.year].append(i.isoformat())

# print(json.dumps(dj, indent=4))

# # объявляем переменные
# string = "Some test string"
# integer = 211
# array = [1, 2, 3, 4, 5]

# # создаем словарь
# mydict = {"title": string, "code": integer, "data": array}

# # сериализуем его в JSON-структуру, как строку
# x = json.dumps(mydict)

# print(x)
