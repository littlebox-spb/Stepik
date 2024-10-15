# put your python code here
def get_path(n):
    if n in [0, 1]:
        return 1
    return get_path(n - 1) + get_path(n - 2)


print(get_path(7))
