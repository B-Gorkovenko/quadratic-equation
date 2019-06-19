from unittest import TestCase, main
from equation import QEquation, NotQuadratic

q = QEquation(1, -5, 4)


class Test(TestCase):
    def test_0_discriminant(self):
        a = 9
        b = q.figure_discriminant()
        self.assertEqual(a, b)

    def test_1_root1(self):
        a = 4
        b = q.figure_root1()
        self.assertEqual(a, b)

    def test_2_root2(self):
        a = 1
        b = q.figure_root2()
        self.assertEqual(a, b)

    def test_not_quadratic(self):
        with self.assertRaises(NotQuadratic):
            QEquation(0, 1, 1)


if __name__ == '__main__':
    main()
