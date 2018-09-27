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
        return self.angle_radians(v) * (Decimal(180.0) / Decimal(pi))

    def magnitude(self):
        return Decimal(sqrt(sum(x**2 for x in self.coordinates)))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise ValueError("Zero vectors can't be normalized")

    def is_zero(self):
        return 0.00 in self.coordinates

    def parallel_with(self, v, tolerance=1e-10):
        if(self.is_zero() or v.is_zero()):
            return True
        return (self.angle_radians(v) == Decimal(0.00) or
                round(self.angle_radians(v), 2) == round(Decimal(pi), 2))

    def orthogonal_with(self, v):
        if(self.is_zero() or v.is_zero()):
            return True
        return self.dot_product(v) == Decimal(0.00)

    def projection_parallel_component(self, v):
        return v.normalized() * self.dot_product(v.normalized()) 

    def projection_orthogonal_component(self, v):
        return self - self.projection_parallel_component(v)