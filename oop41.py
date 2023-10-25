# Напишите определение классов из задания     
class Person:
    def __init__(self,name) -> None:
        self.name=name
        
    def get_name(self):        
        return self.name
    
    def is_employee(self):
        return False
    
class Employee(Person):
    def is_employee(self):
        return True
    

# Ниже располагается код для проверки
assert issubclass(Employee, Person)

p = Person("just human")
assert p.name == 'just human'
assert p.get_name() == 'just human'
assert p.is_employee() is False

emp = Employee("Geek")
assert emp.name == 'Geek'
assert emp.get_name() == 'Geek'
assert emp.is_employee() is True
print('Good')

# # Напишите определение классов из задания     
# class Vehicle:
#     def __init__(self,*args):
#         self.name, self.max_speed, self.mileage = args
        
#     def display_info(self):
#         print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

# class Bus(Vehicle):
#     pass

# # Ниже располагается код для проверки

# assert issubclass(Bus, Vehicle)
# bus_99 = Bus("Ikarus", 66, 124567)
# assert bus_99.name == 'Ikarus'
# assert bus_99.max_speed == 66
# assert bus_99.mileage == 124567
# bus_99.display_info()

# modelX = Vehicle('modelX', 240, 18)
# assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
# modelX.display_info()

# audi = Bus('audi', 123, 43)
# assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
# audi.display_info()