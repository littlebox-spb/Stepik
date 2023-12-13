class DatabaseModelMeta(type):
    def __new__(cls, name, bases, dct):
        cls_obj = super().__new__(cls, name, bases, dct)
        cls_obj.ordering = True
        cls_obj.default_value = None
        return cls_obj


class DatabaseModel(metaclass=DatabaseModelMeta):
    pass


class User(DatabaseModel):
    pass


class Product(DatabaseModel):
    pass


user = User()
product = Product()

print(user.ordering, product.ordering)
user.ordering = False
print(user.ordering, product.ordering)
