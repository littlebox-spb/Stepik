# put your python code here
from datetime import date
import calendar
d = date.fromisoformat(input())
cal= calendar.Calendar()
print(max(cal.itermonthdays(d.year, d.month)))

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