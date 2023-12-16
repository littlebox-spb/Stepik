from datetime import date

from dateutil.relativedelta import relativedelta

d1 = date(2023, 1, 1)
d2 = date(2023, 2, 28)

print(relativedelta(d2, d1))  # relativedelta(months=+1, days=+27)
print(relativedelta(d2, d1).months)  # 1

# import datetime


# def getholiday(year, birthday):
#     try:
#         holiday = datetime.date(year, birthday.month, birthday.day)
#     except ValueError:
#         holiday = datetime.date(year, birthday.month, birthday.day - 1)
#     return holiday


# today = datetime.date.fromisoformat(input())
# birthday = datetime.date.fromisoformat(input())
# holiday = getholiday(today.year, birthday)
# if holiday < today:
#     holiday = getholiday(today.year + 1, birthday)
# delta = holiday - today
# print(delta.days)


# Рекомендации автора курса по чтению

# import datetime

# days = int(input())
# today = datetime.date.fromisoformat(input())

# print(today + datetime.timedelta(days=days))
