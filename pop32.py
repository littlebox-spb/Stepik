import re
import sys

# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
pattern = r"\b(\w)(\w)+?"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r"\2\1", line))

# строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

pattern = r".*\b(\w+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)

# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
pattern = r".*(cat).*\1"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print("------->", line)
