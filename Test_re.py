import re

dim = [
    '<a href="http://stepik.org/courses">',
    "<a href='https://stepik.org'>",
    "<a href='http://neerc.ifmo.ru:1345'>",
    '<a href="ftp://mail.ru/distib" >',
    '<a href="ya.ru">',
    '<a href="www.ya.ru">',
    '<a href="../skip_relative_links">',
    '<a href="ya.ru">',
    '<a href="www.ya.ru">',
    '<a href="../skip_relative_links">',
    '<a href="ya.ru">',
    '<a href="www.ya.ru">',
    '<a href="../skip_relative_links">',
]

pattern = r"<a href=.*//(.+)[/|\'|\:|]"


def domen(s):
    res = re.findall(pattern, s)
    print(res)
    return None if not res else res[0]


assert domen(dim[0]) == "stepik.org"
assert domen(dim[1]) == "stepik.org"
assert domen(dim[2]) == "neerc.ifmo.ru"
assert domen(dim[3]) == "mail.ru"
assert domen(dim[4]) == "ya.ru"
assert domen(dim[5]) == "www.ya.ru"
assert domen(dim[6]) == ""
assert domen(dim[7]) == "ya.ru"
assert domen(dim[8]) == "www.ya.ru"
assert domen(dim[9]) == ""
assert domen(dim[10]) == "ya.ru"
assert domen(dim[11]) == "www.ya.ru"
assert domen(dim[12]) == ""


print("*" * 10, "Good!", "*" * 10, end="")
