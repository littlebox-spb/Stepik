# Напишите определение классов Initialization Vegetarian MeatEater и SweetTooth
class Initialization:
    def __init__(self, capacity, food) -> None:
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print("Количество людей должно быть целым числом")


class Vegetarian(Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)

    def __str__(self) -> str:
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)

    def __str__(self) -> str:
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food) -> None:
        super().__init__(capacity, food)

    def __str__(self) -> str:
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, (int, MeatEater, Vegetarian)):
            return f"Невозможно сравнить количество сладкоежек с {__value}"
        else:
            if isinstance(__value, int):
                return self.capacity == __value
            else:
                return self.capacity == __value.capacity

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, (int, MeatEater, Vegetarian)):
            return f"Невозможно сравнить количество сладкоежек с {__value}"
        else:
            if isinstance(__value, int):
                return self.capacity < __value
            else:
                return self.capacity < __value.capacity

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, (int, MeatEater, Vegetarian)):
            return f"Невозможно сравнить количество сладкоежек с {__value}"
        else:
            if isinstance(__value, int):
                return self.capacity > __value
            else:
                return self.capacity > __value.capacity


# Ниже располагается код для проверки

p1 = Initialization("Chuck", [])
assert isinstance(p1, Initialization)
assert not hasattr(p1, "capacity"), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(p1, "food"), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ["Arkasha"])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ["Arkasha"]

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ["Орехи", "овощи", "фрукты"])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ["nothing"])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ["Жареную картошку", "рыба"])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ["Мороженое", "Чипсы", "ШОКОЛАД"])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимя еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100

# # Напишите определение классов Transport Car Boat и Plane
# # from typing import Optional
# #     def __init__(self, brand, max_speed, kind: Optional[str] = None) -> None:


# class Transport:
#     def __init__(self, brand, max_speed, kind=None) -> None:
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind

#     def __str__(self):
#         return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue) -> None:
#         super().__init__(brand, max_speed, "Car")
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue

#     @property
#     def gasoline(self):
#         return f"Осталось бензина {self.__gasoline_residue} л"

#     @gasoline.setter
#     def gasoline(self, gaz):
#         if isinstance(gaz, int) and not isinstance(gaz, bool):
#             self.__gasoline_residue += gaz
#             print(f"Объем топлива увеличен на {gaz} л и составляет {self.__gasoline_residue} л")
#         else:
#             print("Ошибка заправки автомобиля")


# class Boat(Transport):
#     def __init__(self, brand, max_speed, owners_name) -> None:
#         super().__init__(brand, max_speed, "Boat")
#         self.owners_name = owners_name

#     def __str__(self):
#         return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


# class Plane(Transport):
#     def __init__(self, brand, max_speed, capacity) -> None:
#         super().__init__(brand, max_speed, "Plane")
#         self.capacity = capacity

#     def __str__(self):
#         return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"


# # Ниже располагается код для проверки

# p1 = Transport("Chuck", 50)
# print(p1)
# assert isinstance(p1, Transport)
# assert p1.kind == None
# assert p1.brand == "Chuck"
# assert p1.max_speed == 50
# assert p1.__dict__ == {"kind": None, "brand": "Chuck", "max_speed": 50}

# c1 = Car("RRR", 50, 150, 999)
# print(c1)

# assert isinstance(c1, Car)
# assert c1.kind == "Car"
# assert c1.brand == "RRR"
# assert c1.max_speed == 50
# assert c1.mileage == 150
# assert c1.gasoline == "Осталось бензина 999 л"
# c1.gasoline = 100
# assert c1.gasoline == "Осталось бензина 1099 л"
# assert c1.__dict__ == {"kind": "Car", "brand": "RRR", "max_speed": 50, "mileage": 150, "_Car__gasoline_residue": 1099}

# b1 = Boat("XXX", 1150, "Arkasha")
# print(b1)
# assert isinstance(b1, Boat)
# assert b1.kind == "Boat"
# assert b1.brand == "XXX"
# assert b1.max_speed == 1150
# assert b1.owners_name == "Arkasha"

# pla = Plane("www", 2150, 777)
# print(pla)
# assert isinstance(pla, Plane)
# assert pla.kind == "Plane"
# assert pla.brand == "www"
# assert pla.max_speed == 2150
# assert pla.capacity == 777

# transport = Transport("Telega", 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport("shkolnik", 20, "bike")
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

# first_plane = Plane("Virgin Atlantic", 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
# first_car = Car("BMW", 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Автомобиль успешно заправлен'
# print(first_car.gasoline)  # Осталось бензина на 350 км
# second_car = Car("Audi", 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat("Yamaha", 40, "Petr")
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

# # Напишите определение классов Vehicle Bus и Taxi
# class Vehicle:
#     def __init__(self, name, mileage, capacity) -> None:
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

#     def display(self):
#         print(f"Total {self.name} fare is: {self.fare()}")


# class Bus(Vehicle):
#     def __init__(self, name, mileage) -> None:
#         super().__init__(name, mileage, 50)

#     def fare(self):
#         return super().fare() * 1.1


# class Taxi(Vehicle):
#     def __init__(self, name, mileage) -> None:
#         super().__init__(name, mileage, 4)

#     def fare(self):
#         return super().fare() * 1.35


# # Ниже располагается код для проверки


# sc = Vehicle("Scooter", 100, 2)
# sc.display()

# merc = Bus("Mercedes", 120000)
# merc.display()

# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()

# t = Taxi("x", 111)
# assert t.__dict__ == {"name": "x", "mileage": 111, "capacity": 4}
# t.display()
# b = Bus("t", 123)
# assert b.__dict__ == {"name": "t", "mileage": 123, "capacity": 50}
# b.display()

# # Напишите определение классов Person и Employee
# class Person:
#     def __init__(self, name, passport) -> None:
#         self.name = name
#         self.passport = passport

#     def display(self):
#         print(f"{self.name}: {self.passport}")


# class Employee(Person):
#     def __init__(self, name, passport, salary, department) -> None:
#         super().__init__(name, passport)
#         self.salary = salary
#         self.department = department


# # Ниже располагается код для проверки

# assert issubclass(Employee, Person)

# emp = Person("just human", 123456)
# emp.display()
# assert emp.__dict__ == {"name": "just human", "passport": 123456}

# emp2 = Employee("Geek2", 534432, 321321, "Roga & Koputa")
# emp2.display()
# assert emp2.__dict__ == {"salary": 321321, "department": "Roga & Koputa", "name": "Geek2", "passport": 534432}
