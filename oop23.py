# Напишите определение класса CustomLabel
class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def config(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value


# Ниже код для проверки методов класса CustomLabel
label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
label2 = CustomLabel(text="Username")
label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg="#ffaaaa")
label4 = CustomLabel(text="Hello", bd=20, bg="#ffaaaa")
label5 = CustomLabel(text="qwwerty", a=20, b="#ffaaaa", r=[3, 4, 5, 6], p=32)

assert label1.__dict__ == {"text": "Hello Python", "fg": "#eee", "bg": "#333"}
assert label2.__dict__ == {"text": "Username"}
assert label3.__dict__ == {"text": "Password", "font": ("Comic Sans MS", 24, "bold"), "bd": 20, "bg": "#ffaaaa"}
assert label4.__dict__ == {"text": "Hello", "bd": 20, "bg": "#ffaaaa"}
assert label5.__dict__ == {"text": "qwwerty", "a": 20, "b": "#ffaaaa", "r": [3, 4, 5, 6], "p": 32}

print(label1.__dict__)
print(label2.__dict__)
print(label3.__dict__)
print(label4.__dict__)
print(label5.__dict__)

label4.config(color="red", bd=100)
label5.config(color="red", bd=100, a=32, b=432, p=100, z=432)

assert label4.__dict__ == {"text": "Hello", "bd": 100, "bg": "#ffaaaa", "color": "red"}
assert label5.__dict__ == {
    "text": "qwwerty",
    "a": 32,
    "b": 432,
    "r": [3, 4, 5, 6],
    "p": 100,
    "color": "red",
    "bd": 100,
    "z": 432,
}

# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport

#     def get_info(self):
#         print(f"Worker {self.name}; passport-{self.passport}")


# persons = [
#     ("Allison Hill", 334053, "M", "1635644202"),
#     ("Megan Mcclain", 191161, "F", "2101101595"),
#     ("Brandon Hall", 731262, "M", "6054749119"),
#     ("Michelle Miles", 539898, "M", "1355368461"),
#     ("Donald Booth", 895667, "M", "7736670978"),
#     ("Gina Moore", 900581, "F", "7018476624"),
#     ("James Howard", 460663, "F", "5461900982"),
#     ("Monica Herrera", 496922, "M", "2955495768"),
#     ("Sandra Montgomery", 479201, "M", "5111859731"),
#     ("Amber Perez", 403445, "M", "0602870126"),
# ]

# worker_objects = []

# for i in persons:
#     worker_objects.append(Worker(i[0], i[1], i[2], i[3]))
#     worker_objects[-1].get_info()
