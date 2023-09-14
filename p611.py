os = [len(set(input().split())) for _ in range(int(input()))]
for i in os:
    print(i)


# words = ["mention","soup","pneumonia","tradition","concert","tease","generation","winter","national","jacket",
#     "winter","wrestle","proposal","error","pneumonia","concert","value","value","disclose","glasses","tank",
#     "national","soup","feel","few","concert","wrestle","proposal","soup","sail","brown","service","proposal",
#     "winter","jacket","mention","tradition","value","feel","bear","few","value","winter","proposal","government",
#     "control","value","few","generation","service","national","tradition","government","mention","proposal",
# ]

# sw = set(words)
# cnt = 0
# for i in sw:
#     if len(i) > 6:
#         cnt += 1
# print(cnt)


# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75, 76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31, 33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}

# sa = sorted(list(set_a))
# sb = sorted(list(set_b))

# cnt = ia = ib = 0

# while ia < len(sa) and ib < len(sb):
#     if sa[ia] > sb[ib]:
#         ib += 1
#     elif sa[ia] < sb[ib]:
#         ia += 1
#     else:
#         cnt += 1
#         ia += 1
#         ib += 1


# print(cnt)
