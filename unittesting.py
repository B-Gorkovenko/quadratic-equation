from unittest import TestCase, main
from equation import QEquation, NotQuadratic

q = QEquation(1, -5, 4)
f = QEquation(1, 3, -4) 

class Test(TestCase):
    def test_0_discriminant(self):
        a = 9
        b = q.figure_discriminant()
        a2 = 25
        b2 = f.figure_discriminant()
        self.assertEqual(a, b)
        self.assertEqual(a2, b2)

    def test_1_root1(self):
        a = 4
        b = q.figure_root1()
        self.assertEqual(a, b)
        a2= 1
        b2 = f.figure_root1()
        self.assertEqual(a2, b2)

    def test_2_root2(self):
        a = 1
        b = q.figure_root2()
        self.assertEqual(a, b)
        a2 = -4
        b2 = f.figure_root2()
        self.assertEqual(a2, b2)

    def test_not_quadratic(self):
        with self.assertRaises(NotQuadratic):
            QEquation(0, 1, 1)
            QEquation(0, 6, 8)
            QEquation(0, 7, 9)
            QEquation(0, 6, 3)
            QEquation(0, 2, 4)


if __name__ == '__main__':
    main()
