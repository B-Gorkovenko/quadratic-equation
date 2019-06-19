import math


class NotQuadratic(Exception):
    pass


class QEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0:
            raise NotQuadratic()

    def figure_discriminant(self):
        d = ((self.b)**2) - (4 * self.a * self.c)
        return d

    def figure_root1(self):
        if self.figure_discriminant() < 0:
            return None
        else:
            r1 = (-self.b + math.sqrt(self.figure_discriminant()))\
                 / (2 * self.a)
            return r1

    def figure_root2(self):
        if self.figure_discriminant() < 0:
            return None
        else:
            r2 = (-self.b - math.sqrt(self.figure_discriminant())) \
                 / (2 * self.a)
            return r2


a = QEquation(5, -5, 4)

if __name__ == '__main__':
    print("Первый корень равен: " + str(a.figure_root1()))
    print("Второй корень равен: " + str(a.figure_root2()))
    print("Дискриминант равен: " + str(a.figure_discriminant()))
