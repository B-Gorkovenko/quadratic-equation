import math
import unittest
class QEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        d = ((self.b)**2) - (4 * self.a * self.c)
        return d
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            r1 = (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
            return r1
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            r2 = (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
            return r2

a = QEquation(1,-5,4)
print(a.root1())
print(a.root2())
print(a.discriminant())
