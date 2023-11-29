class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"{self.name} говорит привет"


d = Student("Иван")
print(d.greet())


# input = [1, 2, 4, 1, 6, "e", 45, "e"]


# s = set(input)
# print(len(input) == len(s))
