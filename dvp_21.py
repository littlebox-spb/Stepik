import json
from calendar import monthrange
from datetime import date, datetime, timedelta

data = []
output = {}

fy = int(input())
for i in range(int(input())):
    start, end = map(lambda x: datetime.strptime(x, "%Y-%m-%d"), input().split())
    data.append([start, end])


if len(data) > 1:
    i = 0
    while i < len(data) - 1:
        j = i + 1
        while j < len(data):
            if data[i][1] + timedelta(days=1) == data[j][0]:
                data[i][1] = data[j][1]
                data.remove([data[j][0], data[j][1]])
                j -= 1
            elif data[i][0] <= data[j][0] <= data[i][1]:
                if data[j][1] > data[i][1]:
                    data[i][1] = data[j][1]
                data.remove([data[j][0], data[j][1]])
                j -= 1
            j += 1
        i += 1


def appendMonth(year, numberMonth):
    output[str(numberMonth)].append(
        {
            "start_date": date(year, numberMonth, 1).strftime("%Y-%m-%d"),
            "end_date": date(
                year,
                numberMonth,
                monthrange(year, numberMonth)[1],
            ).strftime("%Y-%m-%d"),
        }
    )


for d in range(len(data)):
    cm = data[d][0].month
    cy = data[d][0].year
    while True:
        if str(cm) not in output and fy == cy:
            output[str(cm)] = []
        if cm != data[d][1].month and cm == data[d][0].month and fy == cy:
            output[str(cm)].append(
                {
                    "start_date": data[d][0].strftime("%Y-%m-%d"),
                    "end_date": date(
                        cy,
                        cm,
                        monthrange(cy, cm)[1],
                    ).strftime("%Y-%m-%d"),
                },
            )
        elif cm < data[d][1].month and fy == cy:
            appendMonth(cy, cm)
        elif cm == data[d][1].month and fy == cy:
            output[str(cm)].append(
                {
                    "start_date": date(cy, cm, 1).strftime("%Y-%m-%d"),
                    "end_date": data[d][1].strftime("%Y-%m-%d"),
                }
            )
            break
        if cm == 12:
            cm = 1
            cy += 1
        else:
            cm += 1


print(json.dumps(output, indent=4))
