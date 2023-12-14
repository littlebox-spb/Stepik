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


output = {}


print(data[0], data[1], sep="\n")
