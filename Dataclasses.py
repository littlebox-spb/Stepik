from dataclasses import dataclass


@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5


stonehenge = Location("Stonehenge", 51, 1.5)

print(stonehenge)

# @dataclass
# class Point:
#     x: int
#     y: int


# point1 = Point(5, 7)
# point2 = Point(-10, 12)

# print(point1, point2, sep="\n")
