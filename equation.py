import math
import unittest
class TestQuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def test_discriminant(self):
        d = ((self.b)**2) - (4 * self.a * self.c)
        return d
        self.assertEqual(d, 0)
    def test_root1(self):
        if self.test_discriminant() < 0:
            return None
        else:
            r1 = -self.b + math.sqrt(self.test_discriminant()) / (2 * self.a)
            return r1
    def test_root2(self):
        if self.test_discriminant() < 0:
            return None
        else:
            r2 = -self.b - math.sqrt(self.test_discriminant()) / (2 * self.a)
            return r2
        self.assertEqual(r2, -1)
a = TestQuadraticEquation(1,2,3)
print(a.test_root1())
print(a.test_root2())
print(a.test_discriminant())

