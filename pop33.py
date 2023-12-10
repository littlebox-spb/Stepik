import re

# import requests

allUrl = []
pattern = r"<a href=.*//(.+)/"

with open("pop33.html", "r", encoding="utf-8") as f:
    while True:
        i = f.readline()
        if not i:
            break
        if re.match(pattern, i):
            allUrl.extend(re.findall(pattern, i))

print(allUrl)


# allUrl1 = []
# allUrl2 = []

# url1, url2 = [input().replace("stepik", "stepic") for _ in range(2)]

# r1 = requests.get(url1)
# allUrl1.extend(re.findall(r'"(.+)"', r1.text))
# for i in allUrl1:
#     r = requests.get(i)
#     allUrl2.extend(re.findall(r'"(.+)"', r.text))

# print("Yes" if url2 in allUrl2 else "No")
