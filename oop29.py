class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
        
    @staticmethod
    def is_positive(N):
        return N>0
    
    @classmethod
    def from_diameter(cls,d):
        return Circle(d/2) if cls.is_positive(d) else None
        
    @staticmethod
    def area(r):
        return 3.14*r*r

# код ниже не нужно удалять, в нем находятся проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56