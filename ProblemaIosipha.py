n = int(input())
k = int(input())

start = [i for i in range(1, n + 1)]

c = 1
while len(start) > 1:
    c += 1
    if c > k:
        start.pop(0)
    temp = start.pop(0)
    start.append(temp)
    if c == k:
        start.pop(0)
        c = 1

print(*start)
