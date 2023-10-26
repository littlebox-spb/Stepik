# Напишите определение класса DictMixin
import json


class DictMixin:
    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda x: x.__dict__))


# Ниже код для проверки миксина DictMixin


class Phone(DictMixin):
    def __init__(self, number):
        self.number = number


class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    "name": "John Doe",
    "age": 30,
    "address": {"street": "123 Main St", "city": "Anytown", "state": "CA", "zip_code": "12345"},
}

address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {
    "address": {"city": "Albuquerque", "state": "NM", "street": "123 Main St", "zip_code": "987654"},
    "age": 30,
    "name": "Walter White",
}

walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {
    "address": {"city": "Albuquerque", "state": "NM", "street": "123 Main St", "zip_code": "987654"},
    "age": 30,
    "name": "Walter White",
    "phone": {"number": "555-1234"},
}

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {
    "address": {"city": "Albuquerque", "state": "NM", "street": "3828 Piermont Dr", "zip_code": "12345"},
    "name": "SCHOOL",
}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {
    "address": {"city": "Albuquerque", "state": "NM", "street": "Los Pollos Hermanos", "zip_code": "12345"},
    "age": 55,
    "friends": [
        {
            "address": {"city": "Albuquerque", "state": "NM", "street": "123 Main St", "zip_code": "987654"},
            "age": 30,
            "name": "Walter White",
            "phone": {"number": "555-1234"},
        },
        {
            "address": {"city": "Albuquerque", "state": "NM", "street": "456 Oak St", "zip_code": "12345"},
            "age": 27,
            "name": "Jesse Bruce Pinkman",
            "phone": {"number": "555-5678"},
        },
    ],
    "name": "Gustavo Fring",
}

print("Good")

# # Напишите определение класса JsonSerializableMixin
# import json


# class JsonSerializableMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__)


# # Ниже код для проверки миксина JsonSerializableMixin
# class Car(JsonSerializableMixin):
#     def __init__(self, make: str, color: str):
#         self.make = make
#         self.color = color


# class Book(JsonSerializableMixin):
#     def __init__(self, title: str, author: str):
#         self.title = title
#         self.author = author


# class Person(JsonSerializableMixin):
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age


# car = Car("Toyota", "red")
# assert car.to_json() == '{"make": "Toyota", "color": "red"}'

# book = Book("The Catcher in the Rye", "J.D. Salinger")
# assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
# book.ratings = [5, 4, 5, 4, 5]
# book.is_bestseller = True
# book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'

# person = Person("John", 30)
# assert person.to_json() == '{"name": "John", "age": 30}'
# print("Good")


# # Напишите определение класса PermissionMixin
# class PermissionMixin:
#     def __init__(self):
#         self.permissions = set()

#     def grant_permission(self, permission):
#         self.permissions.add(permission)

#     def revoke_permission(self, permission):
#         self.permissions.discard(permission)

#     def has_permission(self, permission):
#         return permission in self.permissions


# class User(PermissionMixin):
#     def __init__(self, name, email) -> None:
#         super().__init__()
#         self.name = name
#         self.email = email


# # Ниже код для проверки миксина PermissionMixin

# user1 = User("Alice", "alice@example.com")
# user2 = User("Bob", "bob@example.com")

# assert user1.email == "alice@example.com"
# assert user1.name == "Alice"
# assert user1.permissions == set()

# assert user2.email == "bob@example.com"
# assert user2.name == "Bob"
# assert user2.permissions == set()

# user1.grant_permission("read")
# user1.grant_permission("write")
# user2.grant_permission("read")
# assert user1.permissions == {"read", "write"}
# assert user2.permissions == {"read"}

# assert user1.has_permission("read") is True
# assert user1.has_permission("write") is True
# assert user1.has_permission("execute") is False

# assert user2.has_permission("read") is True
# assert user2.has_permission("write") is False
# assert user2.has_permission("execute") is False

# user1.revoke_permission("write")
# user1.revoke_permission("execute")

# assert user1.has_permission("read") is True
# assert user1.has_permission("write") is False
# assert user1.has_permission("execute") is False

# print("Good")
