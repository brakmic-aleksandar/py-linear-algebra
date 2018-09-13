import unittest
from py_linear_algebra.vector import Vector

class TestVectorMethods(unittest.TestCase):

    def test_addition(self):
        expected_result = Vector([7.089, -7.229999999999999])
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        result = v1 + v2
        self.assertEqual(result, expected_result)

    def test_subtraction(self):
        expected_result = Vector([15.342, 7.337])
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])
        result = v1 - v2
        self.assertEqual(result, expected_result)

    def test_scalar_multiplication(self):
        expected_result = Vector([12.38211, -7.49892, -2.35638])
        v = Vector([1.671, -1.012, -0.318])
        s = 7.41
        result = v * s
        self.assertEqual(result, expected_result)

    def test_magnitude(self):
        expected_result = 7.440282924728065
        result = Vector([-0.221, 7.437]).magnitude()
        self.assertEqual(result, expected_result)
        
    def test_normalization(self):
        expected_result = Vector ([0.9339352140866403, -0.35744232526233])
        result = Vector([5.581, -2.136]).normalized()
        self.assertEqual(result, expected_result)