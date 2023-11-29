import json

# import requests

# response = requests.get(
#     "https://stepik.org/media/attachments/lesson/934800/eq_data_1_day_m1.json"
# )
# with open("files.txt", "wb") as f:
#     f.write(response.content)

magM = [0, 0]
with open("files.txt", "rb") as f:
    data = json.load(f)
    for i in data.items():
        if i[0] == "features":
            for j in range(len(i[1])):
                if i[1][j]["properties"]["mag"] > magM[0]:
                    magM[0] = i[1][j]["properties"]["mag"]
                    magM[1] = i[1][j]["properties"]["place"]
print(magM[1])


# mags = []
# with open("files.txt", "rb") as f:
#     data = json.load(f)
#     for i in data.items():
#         if i[0] == "features":
#             for j in range(10):
#                 mags.append(i[1][j]["properties"]["mag"])
#             break
# print(mags)

# import csv

# import requests

# response = requests.get(
#     "https://stepik.org/media/attachments/lesson/934799/credit_train.csv"
# )
# with open("credit_test.csv", "wb") as f:
#     f.write(response.content)

# with open("credit_test.csv", encoding="utf-8") as r_file:
#     file_reader = csv.reader(r_file, delimiter=",")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             pass
#         else:
#             print(row[7])
#         count += 1
#         if count == 6:
#             break
