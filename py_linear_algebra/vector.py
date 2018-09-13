from math import sqrt

class Vector:
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError
        self.coordinates = tuple(coordinates)
        self.length = len(coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __str__(self):
        return "Vector {}".format(self.coordinates)

    def __add__(self, v):
        self.__assert_compatibility(v)
        newVectorValues = [x + y for x, y in zip(self.coordinates, v.coordinates)] 
        return Vector(newVectorValues)

    def __sub__(self, v):
        self.__assert_compatibility(v)
        newVectorValues = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(newVectorValues)

    def __mul__(self, v):
        newVectorValues = [x * v for x in self.coordinates] 
        return Vector(newVectorValues)

    def __assert_compatibility(self, v):
        if type(v) is not Vector:
            raise TypeError(type(v))
        if(self.length != v.length):
            raise ValueError("Vector dimensions must be same.")

    def magnitude(self):
        return sqrt(sum(x**2 for x in self.coordinates))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (1.0 / magnitude)
        except ZeroDivisionError:
            raise ValueError("Zero vectors can't be normalized")