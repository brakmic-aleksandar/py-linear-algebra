import unittest
from py_linear_algebra.vector import Vector
from decimal import Decimal, getcontext

class TestVectorMethods(unittest.TestCase):

    def test_addition(self):
        getcontext().prec = 10
        expected_result = Vector([7.089, -7.229999999999999])
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        result = v1 + v2
        self.assertAlmostEqual(result.coordinates[0], expected_result.coordinates[0])
        self.assertAlmostEqual(result.coordinates[1], expected_result.coordinates[1])

    def test_subtraction(self):
        expected_result = Vector([15.342, 7.337])
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])
        result = v1 - v2
        self.assertAlmostEqual(result.coordinates[0], expected_result.coordinates[0])
        self.assertAlmostEqual(result.coordinates[1], expected_result.coordinates[1])

    def test_scalar_multiplication(self):
        expected_result = Vector([12.38211, -7.49892, -2.35638])
        v = Vector([1.671, -1.012, -0.318])
        s = 7.41
        result = v * s
        self.assertAlmostEqual(result.coordinates[0], expected_result.coordinates[0])
        self.assertAlmostEqual(result.coordinates[1], expected_result.coordinates[1])
        self.assertAlmostEqual(result.coordinates[2], expected_result.coordinates[2])

    def test_magnitude(self):
        expected_result = Decimal(7.440282924728065)
        result = Vector([-0.221, 7.437]).magnitude()
        self.assertAlmostEqual(result, expected_result)
        
    def test_normalization(self):
        expected_result = Vector ([0.9339352140866403, -0.35744232526233])
        result = Vector([5.581, -2.136]).normalized()
        self.assertAlmostEqual(result.coordinates[0], expected_result.coordinates[0])
        self.assertAlmostEqual(result.coordinates[1], expected_result.coordinates[1])

    def test_dot_product(self):
        expected_result = Decimal(-41.382286)
        v1 = Vector([7.887, 4.138])
        v2 = Vector([-8.802, 6.776])
        result = v1.dot_product(v2)
        self.assertAlmostEqual(result, expected_result)

    def test_angle_radians(self):
        expected_result = Decimal(3.072026309837249)
        v1 = Vector([3.183, -7.627])
        v2 = Vector([-2.668, 5.319])
        result = v1.angle_radians(v2)
        self.assertAlmostEqual(result, expected_result)

    def test_angle_degrees(self):
        expected_result = Decimal(60.27581120523091)
        v1 = Vector([7.35, 0.221, 5.188])
        v2 = Vector([2.751, 8.259, 3.985])
        result = v1.angle_degrees(v2)
        self.assertAlmostEqual(result, expected_result)

    def test_is_zero(self):
        v1 = Vector(['-7.579', '-7.88'])
        self.assertFalse(v1.is_zero())
        v1 = Vector(['0.00', '15.2'])
        self.assertTrue(v1.is_zero())

    def test_parallel_with(self):
        v1 = Vector(['-7.579', '-7.88'])
        v2 = Vector(['22.737', '23.64'])
        self.assertTrue(v1.parallel_with(v2))
        self.assertTrue(v2.parallel_with(v1))
        v1 = Vector(['-2.029', '9.97', '4.172'])
        v2 = Vector(['-9.231', '-6.631', '-7.245'])
        self.assertFalse(v1.parallel_with(v2))
        self.assertFalse(v2.parallel_with(v1))
        v1 = Vector(['2.118', '4.827'])
        v2 = Vector(['0', '0'])
        self.assertTrue(v1.parallel_with(v2))
        self.assertTrue(v2.parallel_with(v1))
    
    def test_orthogonal_with(self):
        v1 = Vector(['-7.579', '-7.88'])
        v2 = Vector(['22.737', '23.64'])
        self.assertFalse(v1.orthogonal_with(v2))
        self.assertFalse(v2.orthogonal_with(v1))
        v1 = Vector(['-2.328', '-7.284', '-1.214'])
        v2 = Vector(['-1.821', '1.072', '-2.94'])
        self.assertTrue(v1.orthogonal_with(v2))
        self.assertTrue(v2.orthogonal_with(v1))
        v1 = Vector(['2.118', '4.827'])
        v2 = Vector(['0', '0'])
        self.assertTrue(v1.orthogonal_with(v2))
        self.assertTrue(v2.orthogonal_with(v1))