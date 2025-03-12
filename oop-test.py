# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (
            type(self.a) in (int, float)
            and type(self.b) in (int, float)
            and type(self.c) in (int, float)
        ):
            return 1
        else:
            return (
                3
                if (
                    self.a < self.b + self.c
                    and self.b < self.a + self.c
                    and self.c < self.a + self.b
                )
                else 2
            )


a, b, c = input().split()  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
