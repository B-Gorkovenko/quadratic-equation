import unittest
import equation as f

q = f.QEquation(1,-5,4)
class Test(unittest.TestCase):
    def test_0_discriminant(self):
        a = 9
        b = q.discriminant()
        self.assertEqual(a, b)

    def test_1_root1(self):
        a = 4
        b = q.root1()
        self.assertEqual(a, b)

    def test_2_root2(self):
        a = 1
        b = q.root2()
        self.assertEqual(a, b)



if __name__ == '__main__':
    unittest.main()