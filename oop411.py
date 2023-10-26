# Создайте классы Database MySQLDatabase и PostgreSQLDatabase

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass


class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    def execute(self, query):
        print(f"Executing query {query} in MySQL database...")


class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

    def execute(self, query):
        print(f"Executing query {query} in PostgreSQL database...")


# Код для проверки

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute("SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute("SELECT * FROM customers;")
postgresql_db.disconnect()

# # Создайте классы Employee HourlyEmployee и SalariedEmployee
# from abc import ABC, abstractmethod


# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass


# class HourlyEmployee(Employee):
#     def __init__(self, hours_worked, hourly_rate) -> None:
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate

#     def calculate_salary(self):
#         return self.hours_worked * self.hourly_rate


# class SalariedEmployee(Employee):
#     def __init__(self, monthly_salary) -> None:
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary


# # Код для проверки

# hourly_employee = HourlyEmployee(100, 25)
# assert hourly_employee.hours_worked == 100
# assert hourly_employee.hourly_rate == 25
# assert hourly_employee.calculate_salary() == 2500

# salaried_employee = SalariedEmployee(4000)
# assert salaried_employee.monthly_salary == 4000
# assert salaried_employee.calculate_salary() == 4000
# print("Good")
