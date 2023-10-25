# Напишите определение классов Person Company Employee
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")


class Company:
    def __init__(self, company_name, location) -> None:
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location) -> None:
        super().__init__(name, age)
        Company.__init__(self, company_name, location)


# Ниже расположены провевки для кода


a = Person("Ivan", 32)
a.display_person_info()

a = Company("Zara", "Prague")
a.display_company_info()

emp = Employee("Jessica", 28, "Google", "Atlanta")
emp.display_person_info()
emp.display_company_info()

emp2 = Employee("Kolya", 11, "Facebook", "Seatle")
emp2.display_person_info()
emp2.display_company_info()

# # Напишите определение классов User Authentication AuthenticatedUser
# class User:
#     def __init__(self, user, password) -> None:
#         self.user = user
#         self.password = password

#     def get_info(self):
#         return f"Имя пользователя: {self.user}"


# class Authentication:
#     def authenticate(self, user, password):
#         return self.user == user and self.password == password


# class AuthenticatedUser(User, Authentication):
#     pass


# # Ниже расположены провевки для кода


# assert issubclass(AuthenticatedUser, User) is True
# assert issubclass(AuthenticatedUser, Authentication) is True

# user1 = AuthenticatedUser("user1", "password1")
# assert user1.get_info() == "Имя пользователя: user1"
# assert user1.authenticate("user1", "password2") is False
# assert user1.authenticate("user1", "password1") is True

# ted = AuthenticatedUser("ted_lawyer", "alligator3")
# print(ted.get_info())
