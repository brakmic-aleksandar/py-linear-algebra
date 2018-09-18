from math import sqrt
from math import acos
from math import pi
from decimal import Decimal, getcontext

class Vector:
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError
        self.coordinates = tuple(Decimal(x) for x in coordinates)
        self.length = len(coordinates)

    def __eq__(self, v):
        self.coordinates == v.coordinates

    def __str__(self):
        return "Vector {}".format(self.coordinates)

    def __add__(self, v):
        self.__assert_compatibility(v)
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)] 
        return Vector(new_coordinates)

    def __sub__(self, v):
        self.__assert_compatibility(v)
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v):
        new_coordinates = self.multiply_scalar(Decimal(v))
        return Vector(new_coordinates)

    def __assert_compatibility(self, v):
        if type(v) is not Vector:
            raise TypeError(type(v))
        if(self.length != v.length):
            raise ValueError("Vector dimensions must be same.")

    def multiply_scalar(self, s):
        return [x * s for x in self.coordinates] 

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_radians(self, v):
        try:
            return Decimal(acos(self.normalized().dot_product(v.normalized())))
        except ValueError:
            raise ValueError("Can't find angle if one of vectors is zero vector")

    def angle_degrees(self, v):
        return self.angle_radians(v) * Decimal(180.0 / pi)

    def magnitude(self):
        return Decimal(sqrt(sum(x**2 for x in self.coordinates)))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise ValueError("Zero vectors can't be normalized")


expected_result = Vector([7.089, -7.229999999999999])
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
result = v1 + v2
print(result, expected_result)

expected_result = Vector([15.342, 7.337])
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])
result = v1 - v2
print(result, expected_result)

expected_result = Vector([12.38211, -7.49892, -2.35638])
v = Vector([1.671, -1.012, -0.318])
s = 7.41
result = v * s
print(result, expected_result)

expected_result = 7.440282924728065
result = Vector([-0.221, 7.437]).magnitude()
print(result, expected_result)

expected_result = Vector ([0.9339352140866403, -0.35744232526233])
result = Vector([5.581, -2.136]).normalized()
print(result, expected_result)

expected_result = -41.382286
v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
result = v1.dot_product(v2)
print(result, expected_result)

expected_result = 3.072026309837249
v1 = Vector([3.183, -7.627])
v2 = Vector([-2.668, 5.319])
result = v1.angle_radians(v2)
print(result, expected_result)

expected_result = 60.27581120523091
v1 = Vector([7.35, 0.221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])
result = v1.angle_degrees(v2)
print(result, expected_result)