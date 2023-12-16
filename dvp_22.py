import datetime

from dateutil.relativedelta import relativedelta


def namemon(month):
    if month == 1:
        return "месяц"
    elif 2 <= month <= 4:
        return "месяца"
    else:
        return "месяцев"


def nameyear(year):
    if year == 1:
        return "год"
    elif 2 <= year <= 4:
        return "года"
    else:
        return "лет"


def nameday(day):
    if day == 1:
        return "день"
    elif 2 <= day <= 4:
        return "дня"
    else:
        return "дней"


d1 = datetime.date.fromisoformat(input())
d2 = datetime.date.fromisoformat(input())
if d1 != d2:
    result = relativedelta(d2, d1)
    oyear = f"{result.years} {nameyear(result.years)} " if result.years else ""
    omonth = f"{result.months} {namemon(result.months)} " if result.months else ""
    oday = f"{result.days} {nameday(result.days)}" if result.days else ""
    print(f"{oyear}{omonth}{oday}")
else:
    print(f"Менее дня")

# Решение чужое, надо разбираться, как сделано
#
# from datetime import date
# from dateutil import relativedelta


# def get_word(n: int, form1: str, form2:str, form3: str) -> str:
#     if not n:
#         return ''
#     res = form3
#     if n % 10 == 1 and n != 11:
#         res = form1
#     elif 0 < n % 10 < 5 and not (10 <= n <= 20) and n != 0:
#         res = form2
#     return f'{n} {res} '

# word_forms = ('год', "года", "лет"), ('месяц', "месяца", "месяцев"), ("день", "дня", "дней")
# start, end = map(date.fromisoformat, map(str.strip, open(0)))
# time_diff = relativedelta.relativedelta(end, start)
# diffs = (time_diff.years, time_diff.months, time_diff.days)
# res = ''
# if not any(diffs):
#     print('Менее дня')
# else:
#     for n, forms in zip(diffs, word_forms):
#         res += get_word(n, *forms)
#     print(res.strip())


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
