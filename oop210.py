class User:
    
    def __init__(self,name,role):
        self.name=name
        self.role=role
        
class Access:
    __access_list=['admin', 'developer']
    
    @staticmethod
    def __check_access(role):
        return role in Access.__access_list
    
    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            print(f'User {user.name}: success' if Access.__check_access(user.role) else f'AccessDenied')
        else:
            print('AccessTypeError')



user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError


# class Robot:
#     population=0
    
#     def __init__(self,name):
#         self.name=name
#         Robot.population+=1
#         print(f'Робот {name} был создан')
        
#     def destroy(self):
#         Robot.population-=1
#         print(f'Робот {self.name} был уничтожен')
        
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
        
#     @classmethod        
#     def how_many(cls):
#         print(f'{cls.population}, вот сколько нас еще осталось')

# # код ниже не нужно удалять, в нем находятся проверки

# droid1 = Robot("R2-D2")
# assert droid1.name == 'R2-D2'
# assert Robot.population == 1
# droid1.say_hello()
# Robot.how_many()
# droid2 = Robot("C-3PO")
# assert droid2.name == 'C-3PO'
# assert Robot.population == 2
# droid2.say_hello()
# Robot.how_many()
# droid1.destroy()
# assert Robot.population == 1
# droid2.destroy()
# assert Robot.population == 0
# Robot.how_many()