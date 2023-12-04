import re

test = "Дополните образец регулярного выражения для поиска color и colour используя группы."
pattern = r"colo.?r"
print(test)
print(re.sub(pattern, "+", test))
