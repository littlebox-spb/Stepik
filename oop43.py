# class Square:
#     def get_value(self, a):
#         return a * a       
    
# class Cube(Square):
#     def get_value(self, a):
#         return a**3

# class Power4(Square):
#     def get_value(self, a):
#         return a**4

# # Напишите определение классов Cube и Power4  

# assert issubclass(Cube, Square)
# assert issubclass(Power4, Square)

# cube = Cube()
# assert cube.get_value(2) == 8
# assert cube.get_value(-17) == -4913

# power4 = Power4()
# assert power4.get_value(5) == 625
# assert power4.get_value(25) == 390625

# print('Good')


class MethodOverriding:
    def __init__(self):
        x = X()
        y = Y()
        y.method_2()
        x.method_1()
        y.method_1()
        x = y
        x.method_1() # № 1
        x.method_2() # № 2


class X:
    def method_1(self):
        print("m1 ~ X")


class Y(X):
    def method_1(self):
        print("m1 ~ Y")

    def method_2(self):
        print("m2 ~ Y")


MethodOverriding()
