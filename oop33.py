class Vector:
    
    def __init__(self,*args) -> None:
        self.values=[]
        for n in args:
            if isinstance(n,int) and not isinstance(n,bool):
                self.values.append(n)
        self.values.sort()

    def __str__(self) -> str:
        if len(self.values)==0:
            return 'Пустой вектор'
        else:
            return 'Вектор('+', '.join([str(n) for n in self.values])+')'

    def __add__(self,other):
        newVector=self.values.copy()
        if isinstance(other,int) and not isinstance(other,bool):
            for i in range(len(self.values)):
                newVector[i]+=other
            return Vector(*newVector)
        elif isinstance(other,Vector):
            if len(self.values)==len(other.values):
                for i in range(len(self.values)):
                    newVector[i]+=other.values[i]
                return Vector(*newVector)            
            else:
                print('Сложение векторов разной длины недопустимо')
        print(f'Вектор нельзя сложить с {other}')

    def __mul__(self,other):
        newVector=self.values.copy()
        if isinstance(other,int) and not isinstance(other,bool):
            for i in range(len(self.values)):
                newVector[i]*=other
            return Vector(*newVector)
        elif isinstance(other,Vector):
            if len(self.values)==len(other.values):
                for i in range(len(self.values)):
                    newVector[i]*=other.values[i]
                return Vector(*newVector)            
            else:
                print('Умножение векторов разной длины недопустимо')
        print(f'Вектор нельзя умножать с {other}')

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"

# # Напишите определение класса Order       
# class Order:
#     def __init__(self,cart, customer) -> None:
#         self.cart=cart
#         self.customer=customer

#     def __add__(self,cart):
#         return Order(self.cart+[cart],self.customer)

#     def __radd__(self,cart):
#         return Order([cart]+self.cart,self.customer)

#     def __sub__(self,cart):
#         newCart=self.cart.copy()
#         if cart in newCart:
#             newCart.remove(cart)
#         return Order(newCart,self.customer)

#     def __rsub__(self,cart):
#         return self - cart

# # Ниже код для проверки методов класса Order

# order = Order(['banana', 'apple'], 'Гена Букин')

# order_2 = order + 'orange'
# assert order.cart == ['banana', 'apple']
# assert order.customer == 'Гена Букин'
# assert order_2.cart == ['banana', 'apple', 'orange']

# order = 'mango' + order
# assert order.cart == ['mango', 'banana', 'apple']
# order = 'ice cream' + order
# assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

# order = order - 'banana'
# assert order.cart == ['ice cream', 'mango', 'apple']

# order3 = order - 'banana'
# assert order3.cart == ['ice cream', 'mango', 'apple']

# order = order - 'mango'
# assert order.cart == ['ice cream', 'apple']
# order = 'lime' - order
# assert order.cart == ['ice cream', 'apple']
# print('Good')

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

#     def __mul__(self, other):
#         return self.x * other.x + self.y * other.y


# v1 = Vector(2, 3)
# v2 = Vector(4, 3)

# print(v1*v2)

# # Напишите определение класса Rectangle       
# class Rectangle:
#     def __init__(self,width,height) -> None:
#         self.width=width
#         self.height=height
        
#     def __add__(self,rectangle):
#         return Rectangle(self.width+rectangle.width, self.height+rectangle.height)        
    
#     def __str__(self) -> str:
#         return f'Rectangle({self.width}x{self.height})'

# # Ниже код для проверки методов класса Rectangle

# r1 = Rectangle(5, 10)
# assert r1.width == 5
# assert r1.height == 10
# print(r1)

# r2 = Rectangle(20, 5)
# assert r2.width == 20
# assert r2.height == 5
# print(r2)

# r3 = r2 + r1
# assert isinstance(r3, Rectangle)
# assert r3.width == 25
# assert r3.height == 15
# print(r3)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __radd__(self, other):
#         if isinstance(other, Number):
#             return Vector(self.x + other.value, self.y + other.value)

#     def __str__(self):
#         return f"Vector({self.x},{self.y})"


# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Number(other.x + other.y + self.value)

#     def __str__(self):
#         return f"Number({self.value})"


# v = Vector(2, 3)
# num = Number(5)
# print(num + v)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __radd__(self, other):
#         if isinstance(other, Number):
#             return Vector(self.x + other.value, self.y + other.value)

#     def __str__(self):
#         return f"Vector({self.x},{self.y})"


# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"Number({self.value})"


# v = Vector(2, 3)
# num = Number(5)
# print(num + v)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Number):
#             return Vector(self.x + other.value, self.y + other.value)

#     def __str__(self):
#         return f"Vector({self.x},{self.y})"


# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __radd__(self, other):
#         if isinstance(other, Vector):
#             return Number(other.x + other.y + self.value)

#     def __str__(self):
#         return f"Number({self.value})"


# v = Vector(2, 3)
# num = Number(5)
# print(num + v)

# class MyPoint:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)


# p1 = MyPoint(3, 4)
# p2 = MyPoint(5, 12)
# p3 = p1 + p2
# print(p3.x + p3.y)