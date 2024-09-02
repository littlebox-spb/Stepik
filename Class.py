from random import choice, random


class Fig:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

    def clear(self):
        pass

    def __str__(self) -> str:
        return f"{self.sp} - {self.ep}"


class Line(Fig):
    def clear(self):
        self.sp = (0, 0)
        self.ep = (0, 0)


class Rect(Fig):
    pass


class Ellipse(Fig):
    pass


elements = []
for _ in range(217):
    choices = [Line, Rect, Ellipse]
    elements.append(choice(choices)(random(), random(), random(), random()))

for i in elements:
    i.clear()

print([str(i) for i in elements])
