import json


# Напишите определение класса AppConfig
class AppConfig:
    myConfig = {}

    @classmethod
    def load_config(cls, fname):
        with open(fname, "r") as file:
            cls.myConfig = json.loads(file.read())

    @classmethod
    def isValidParam(cls, key):
        test = key[0] in cls.myConfig
        if len(key) > 1:
            if test and key[1] in cls.myConfig[key[0]]:
                return test
            else:
                test = False
        return test

    @classmethod
    def get_config(cls, param):
        key = param.split(".")
        result = None
        if cls.isValidParam(key):
            result = (
                cls.myConfig[key[0]][key[1]] if len(key) > 1 else cls.myConfig[key[0]]
            )
        return result


# Загрузка конфигурации при запуске приложения
AppConfig.load_config("app_config.json")

# Получение значения конфигурации
assert AppConfig.get_config("database") == {
    "host": "127.0.0.1",
    "port": 5432,
    "database_name": "postgres_db",
    "user": "owner",
    "password": "ya_vorona_ya_vorona",
}
assert AppConfig.get_config("database.user") == "owner"
assert AppConfig.get_config("database.password") == "ya_vorona_ya_vorona"
assert AppConfig.get_config("database.pass") is None
assert AppConfig.get_config("password.database") is None

config = AppConfig()
assert config.get_config("max_connections") == 10
assert config.get_config("min_connections") is None

conf = AppConfig()
assert conf.get_config("max_connections") == 10
assert conf.get_config("database.user") == "owner"
assert conf.get_config("database.host") == "127.0.0.1"
assert conf.get_config("host") is None

print("Good")

# class Circle:

#     def __init__(self, radius):
#         if not Circle.is_positive(radius):
#             raise ValueError("Радиус должен быть положительным")
#         self.radius = radius

#     @staticmethod
#     def is_positive(N):
#         return N>0

#     @classmethod
#     def from_diameter(cls,d):
#         return Circle(d/2) if cls.is_positive(d) else None

#     @staticmethod
#     def area(r):
#         return 3.14*r*r

# # код ниже не нужно удалять, в нем находятся проверки
# circle_1 = Circle.from_diameter(10)
# assert isinstance(circle_1, Circle)
# assert circle_1.radius == 5.0
# print(f"circle_1.radius={circle_1.radius}")
# assert Circle.is_positive(10)
# assert not Circle.is_positive(-5)
# assert Circle.area(1) == 3.14
# assert Circle.area(2) == 12.56
