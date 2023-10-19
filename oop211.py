# class File:

#     def __init__(self,name) -> None:
#         self.name=name
#         self.in_trash=False
#         self.is_deleted=False

#     def restore_from_trash(self):
#         self.in_trash=False
#         print(f'Файл {self.name} восстановлен из корзины')

#     def remove(self):
#         self.is_deleted=True
#         print(f'Файл {self.name} был удален')

#     def read(self):
#         if self.is_deleted:
#             print(f'ErrorReadFileDeleted({self.name})')
#         elif self.in_trash:
#             print(f'ErrorReadFileTrashed({self.name})')
#         else:
#             print(f'Прочитали все содержимое файла {self.name}')

#     def write(self,content):
#         if self.is_deleted:
#             print(f'ErrorWriteFileDeleted({self.name})')
#         elif self.in_trash:
#             print(f'ErrorWriteFileTrashed({self.name})')
#         else:
#             print(f'Записали значение {content} в файл {self.name}')

# class Trash:

#     content=[]

#     @staticmethod
#     def add(f):
#         if isinstance(f,File):
#             Trash.content.append(f)
#             f.in_trash=True
#         else:
#             print('В корзину добавлять можно только файл')

#     @staticmethod
#     def clear():
#         print('Очищаем корзину')
#         while len(Trash.content)>0:
#             f=Trash.content.pop(0)
#             f.remove()
#         print('Корзина пуста')

#     @staticmethod
#     def restore():
#         print('Восстанавливаем файлы из корзины')
#         while len(Trash.content)>0:
#             f=Trash.content.pop(0)
#             f.restore_from_trash()
#         print('Корзина пуста')

# # Ниже код для проверки класса File и Trash

# f1 = File('puppies.jpg')
# f2 = File('cat.jpg')
# f3 = File('xxx.doc')
# passwords = File('pass.txt')

# for file in [f1, f2, f3, passwords]:
#     assert file.is_deleted is False
#     assert file.in_trash is False

# f3.read()
# f3.remove()
# assert f3.is_deleted is True
# f3.read()
# f3.write('hello')

# assert Trash.content == []

# Trash.add(f2)
# Trash.add(passwords)
# Trash.add(f3)

# f1.read()
# Trash.add(f1)
# f1.read()

# for file in [f1, f2, f3, passwords]:
#     assert file.in_trash is True

# for f in [f2, passwords, f3, f1]:
#     assert f in Trash.content

# Trash.restore()
# assert Trash.content == [], 'После восстановления корзина должна была очиститься'

# Trash.add(passwords)
# Trash.add(f2)
# Trash.add('hello')
# Trash.add(f1)

# for f in [passwords, f2, f1]:
#     assert f in Trash.content


# Trash.clear()

# for file in [passwords, f2, f1]:
#     assert file.is_deleted is True

# assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

# f1.read()


# import string

# # Напишите определение класса Registration
# class Registration:
#     def __init__(self, l,p):
#         self.login = l
#         self.password = p

#     @property
#     def login(self):
#         return self.__login

#     @property
#     def password(self):
#         return self.__password

#     @login.setter
#     def login(self, l):
#         if not isinstance(l, str):
#             raise TypeError
#         t = [s for s in l if s in ["@", "."]]
#         if len(t) <= 1 or len(t) > 2:
#             raise ValueError
#         if t == ["@", "@"]:
#             raise ValueError
#         if t == [".", "."]:
#             raise ValueError
#         if t == [".", "@"]:
#             raise ValueError
#         self.__login = l

#     @staticmethod
#     def is_include_digit(p):
#         for i in p:
#             if i in '0123456789':
#                 return True
#         return False

#     @staticmethod
#     def is_include_all_register(p):
#         if p==p.lower() or p==p.upper():
#             return False
#         else:
#             return True

#     @staticmethod
#     def is_include_only_latin(p):
#         for i in p:
#             if (i not in '0123456789') and (i not in string.ascii_letters):
#                 return False
#         return True

#     @staticmethod
#     def check_password_dictionary(p):
#         with open('easy_passwords.txt','r',encoding='utf-8') as f:
#             for line in f:
# #                g=f.readline()[:-2]
#                 if line[:-1]==p:
#                     f.close
#                     return True
#         return False

#     @password.setter
#     def password(self, p):
#         if not isinstance(p, str):
#             raise TypeError
#         if not (4<len(p)<12):
#             raise ValueError
#         if not Registration.is_include_digit(p):
#             raise ValueError
#         if not Registration.is_include_all_register(p):
#             raise ValueError
#         if not Registration.is_include_only_latin(p):
#             raise ValueError
#         if Registration.check_password_dictionary(p):
#             raise ValueError
#         self.__password = p


# # Ниже код для проверки класса Registration


# try:
#     s2 = Registration("fga", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

# try:
#     s2 = Registration("fg@a", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

# s2 = Registration("translate@gmail.com", "as1SNdf")
# try:
#     s2.login = "asdsa12asd."
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12asd как можно записать такой логин?")

# try:
#     s2.login = "asdsa12@asd"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12@asd как можно записать такой логин?")

# assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


# try:
#     s2.password = "KissasSAd1f"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

# try:
#     s2.password = "124244242"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "RYIWUhjkdbfjfgdsffds"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "CaT"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "monkey"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

# try:
#     s2.password = "HelloQEWq"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

# try:
#     s2.password = [4, 32]
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")

# try:
#     s2.password = 123456
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")

# print('U r hacked Pentagon')
