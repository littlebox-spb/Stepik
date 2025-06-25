# ******************************************
# Сетка записи
# Задача курса https://stepik.org/lesson/922338/step/3?unit=928217
# ******************************************
from datetime import datetime

schedule = {}


def get_weekday(date_string: str) -> dict:
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M")
    return {"week": date.weekday(), "time": date.time()}


def get_time(time_string: str) -> dict:
    date = datetime.strptime(time_string, "%H:%M")
    return {"time": date.time()}


for i in range(5):
    time_start, time_end = map(get_time, input().split())
    schedule[i] = {"start": time_start, "end": time_end}
record_start, record_end = map(get_weekday, input().split())
if record_start["week"] != record_end["week"] or record_start["week"] in (5, 6):
    print("False")
elif (
    schedule[record_start["week"]]["start"]["time"] <= record_start["time"]
    and record_end["time"] <= schedule[record_start["week"]]["end"]["time"]
):
    print("True")
else:
    print("False")
