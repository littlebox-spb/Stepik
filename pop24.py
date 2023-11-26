import os

out = []
for s in os.walk("sample"):
    for i in s[-1]:
        if i.endswith(".py"):
            out.append(s[0].replace("\\", "/"))
            break

with open("ans.txt", "w") as f:
    f.write(str("\n".join(out)))

print(str("\n".join(out)))

# with open("dataset_24465_4.txt") as rd, open("dataset_24465_4o.txt", "w") as wc:
#     buf = []
#     for i in rd.readlines():
#         buf.append(i.rstrip())
#     for i in range(len(buf)):
#         wc.write(buf[len(buf) - 1 - i])
#         wc.write("\n")
