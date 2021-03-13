import unittest
import mathlib


class MathLibTests(unittest.TestCase):

    #Test of function add
    def test_add(self):

        #Integer
        self.assertEqual(mathlib.add(12, 30), 42)
        self.assertEqual(mathlib.add(12, -12), 0)
        self.assertEqual(mathlib.add(-4, 5), 1)
        self.assertEqual(mathlib.add(-3, -2), -5)
        self.assertEqual(mathlib.add(24, 0), 24)
        self.assertEqual(mathlib.add(-9, 0), -9)
        self.assertEqual(mathlib.add(0, 0), 0)

        #Decimal
        self.assertEqual(mathlib.add(1.5, 8), 9.5)
        self.assertEqual(mathlib.add(10.1, 9.3), 19.4)
        self.assertEqual(mathlib.add(42.123, 12.32), 54.443)
        self.assertEqual(mathlib.add(-11, 5.45), -5.55)
        self.assertEqual(mathlib.add(42.4242424242, -42.4242424242), 0)
        self.assertEqual(mathlib.add(-3.73, -21.9871474), -25.7171474)
        self.assertEqual(mathlib.add(666.666, 0), 666.666)
        self.assertEqual(mathlib.add(0, -44.9845), -44.9845)


    #Test of function sub
    def test_sub(self):

        self.assertEqual(mathlib.sub(61, 21), 40)

    #Test of function mul
    def test_mul(self):

        self.assertEqual(mathlib.mul(12, 2), 24)

    #Test of function div
    def test_div(self):

        self.assertEqual(mathlib.div(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
