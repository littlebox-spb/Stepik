inp = "8 11 -6 3 0 1 1"


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def recSortSli(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = recSortSli(lst[:mid])
        right = recSortSli(lst[mid:])
        return merge(left, right)


lst = list(map(int, inp.split()))
print(*recSortSli(lst))
