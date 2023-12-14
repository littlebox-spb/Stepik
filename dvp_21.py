from calendar import monthrange
from datetime import date, datetime

data = []

y = 2022
# 2
interval1 = "2022-02-20 2022-03-05"
interval2 = "2022-03-20 2022-04-10"

start, end = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), interval1.split())
data.append([start, end])
start, end = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), interval2.split())
data.append([start, end])

for d in range(len(data)):
    print(data[d])
    if data[d][0].month != data[d][1].month:
        print("нужно бить интервал")
        print("последний день", monthrange(data[d][0].year, data[d][0].month)[1])
