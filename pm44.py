try:
    v = float(input())
except TypeError:
    print("Неверне значение, повторите ввод данных!")
finally:
    if v <= 0.0:
        print("Введен неверный возраст")
    else:
        print(round(v * 10.5, 1) if v <= 2.0 else round(2 * 10.5 + (v - 2) * 4, 1))

    # if v <= 2.0:
    #     print(round(v * 10.5, 1))
    # else:
    #     print(round(2 * 10.5 + (v - 2) * 4, 1))


# Zodiak = {
#     "Козерог": [{"day": 22, "mon": "декабрь"}, {"day": 19, "mon": "январь"}],
#     "Водолей": [{"day": 20, "mon": "январь"}, {"day": 18, "mon": "февраль"}],
#     "Рыбы": [{"day": 19, "mon": "февраль"}, {"day": 20, "mon": "март"}],
#     "Овен": [{"day": 21, "mon": "март"}, {"day": 19, "mon": "апреля"}],
#     "Телец": [{"day": 20, "mon": "апреля"}, {"day": 20, "mon": "май"}],
#     "Близнецы": [{"day": 21, "mon": "май"}, {"day": 20, "mon": "июнь"}],
#     "Рак": [{"day": 21, "mon": "июнь"}, {"day": 22, "mon": "июль"}],
#     "Лев": [{"day": 23, "mon": "июль"}, {"day": 22, "mon": "август"}],
#     "Дева": [{"day": 23, "mon": "август"}, {"day": 22, "mon": "сентябрь"}],
#     "Весы": [{"day": 23, "mon": "сентябрь"}, {"day": 22, "mon": "октябрь"}],
#     "Скорпион": [{"day": 23, "mon": "октябрь"}, {"day": 21, "mon": "ноябрь"}],
#     "Стрелец": [{"day": 22, "mon": "ноябрь"}, {"day": 21, "mon": "декабрь"}],
# }
# d, m = int(input()), input()
# for z, per in Zodiak.items():
#     if per[0]["mon"] == m or per[1]["mon"] == m:
#         if (per[0]["mon"] == m and d >= per[0]["day"]) or (
#             per[1]["mon"] == m and d <= per[1]["day"]
#         ):
#             print(z)
#             break