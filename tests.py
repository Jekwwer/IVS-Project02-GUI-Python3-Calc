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
        self.assertEqual(mathlib.add(0, -9), -9)
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

        #Integer
        self.assertEqual(mathlib.sub(12, 30), -18)
        self.assertEqual(mathlib.sub(12, -12), 24)
        self.assertEqual(mathlib.sub(-4, 5), -9)
        self.assertEqual(mathlib.sub(-3, -2), -1)
        self.assertEqual(mathlib.sub(24, 0), 24)
        self.assertEqual(mathlib.sub(0, -9), 9)
        self.assertEqual(mathlib.sub(0, 0), 0)

        # Decimal
        self.assertEqual(mathlib.sub(1.5, 8), -6.5)
        self.assertAlmostEqual(mathlib.sub(10.1, 9.3), 0.8, 1)
        self.assertAlmostEqual(mathlib.sub(42.123, 12.32), 29.803, 3)
        self.assertEqual(mathlib.sub(-11, 5.45), -16.45)
        self.assertEqual(mathlib.sub(42.4242424242, -42.4242424242), 84.8484848484)
        self.assertEqual(mathlib.sub(-3.73, -21.9871474), 18.2571474)
        self.assertEqual(mathlib.sub(666.666, 0), 666.666)
        self.assertEqual(mathlib.sub(0, -44.9845), 44.9845)


    #Test of function mul
    def test_mul(self):

        #Integer
        self.assertEqual(mathlib.mul(12, 30), 360)
        self.assertEqual(mathlib.mul(12, -12), -144)
        self.assertEqual(mathlib.mul(-4, 5), -20)
        self.assertEqual(mathlib.mul(-3, -2), 6)
        self.assertEqual(mathlib.mul(24, 0), 0)
        self.assertEqual(mathlib.mul(0, -9), 0)
        self.assertEqual(mathlib.mul(0, 0), 0)

        # Decimal
        self.assertEqual(mathlib.mul(1.5, 8), 12)
        self.assertEqual(mathlib.mul(10.1, 9.3), 93.93)
        self.assertAlmostEqual(mathlib.mul(42.123, 12.32), 518.95536, 5)
        self.assertEqual(mathlib.mul(-11, 5.45), -59.95)
        self.assertAlmostEqual(mathlib.mul(42.4242424242, -42.4242424242), -1799.816345267, 9)
        self.assertAlmostEqual(mathlib.mul(-3.73, -21.9871474), 82.012059802, 9)
        self.assertEqual(mathlib.mul(666.666, 0), 0)
        self.assertEqual(mathlib.mul(0, -44.9845), 0)


    #Test of function div
    def test_div(self):

        #Cannot divide by zero
        with self.assertRaises(ValueError):
            mathlib.div(24, 0)
        with self.assertRaises(ValueError):
            mathlib.div(-8, 0)
        with self.assertRaises(ValueError):
            mathlib.div(666.666, 0)
        with self.assertRaises(ValueError):
            mathlib.div(0, 0)

        #Integer
        self.assertEqual(mathlib.div(12, 30), 0.4)
        self.assertEqual(mathlib.div(12, -12), -1)
        self.assertEqual(mathlib.div(-4, 5), -0.8)
        self.assertEqual(mathlib.div(-3, -2), 1.5)
        self.assertEqual(mathlib.div(0, -9), 0)

        # Decimal
        self.assertEqual(mathlib.div(1.5, 8), 0.1875)
        self.assertAlmostEqual(mathlib.div(10.1, 9.3), 1.086021505, 9)
        self.assertAlmostEqual(mathlib.div(42.123, 12.32), 3.419074675, 9)
        self.assertAlmostEqual(mathlib.div(-11, 5.45), -2.018348624, 9)
        self.assertEqual(mathlib.div(42.4242424242, -42.4242424242), -1)
        self.assertAlmostEqual(mathlib.div(-3.73, -21.9871474), 0.169644562, 9)
        self.assertEqual(mathlib.div(0, -44.9845), 0)


    #Test of function fac
    def test_fac(self):

        #Factorial of negative or decimal number cannot be calculated.
        with self.assertRaises(ValueError):
            mathlib.fac(-1)
        with self.assertRaises(ValueError):
            mathlib.fac(-10)
        with self.assertRaises(ValueError):
            mathlib.fac(24.24)
        with self.assertRaises(ValueError):
            mathlib.fac(-4.2)

        #Integer >= 0
        self.assertEqual(mathlib.fac(0), 1)
        self.assertEqual(mathlib.fac(1), 1)
        self.assertEqual(mathlib.fac(4), 24)
        self.assertEqual(mathlib.fac(10), 3628800)
        self.assertEqual(mathlib.fac(15), 1307674368000)

if __name__ == '__main__':
    unittest.main()
