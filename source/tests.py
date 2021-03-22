##
# @file tests.py
# @brief Tests of mathematical library
# @author Pavel Beneš (xbenes58)
# @date 2021-03-20


import unittest
import math_lib as mathlib  # our mathematical library


class MathLibTests(unittest.TestCase):

    # Test of function add
    def test_add(self):

        # Integer
        self.assertEqual(mathlib.add(12, 30), 42)
        self.assertEqual(mathlib.add(12, -12), 0)
        self.assertEqual(mathlib.add(-4, 5), 1)
        self.assertEqual(mathlib.add(-3, -2), -5)
        self.assertEqual(mathlib.add(24, 0), 24)
        self.assertEqual(mathlib.add(0, -9), -9)
        self.assertEqual(mathlib.add(0, 0), 0)

        # Decimal
        self.assertEqual(mathlib.add(1.5, 8), 9.5)
        self.assertEqual(mathlib.add(10.1, 9.3), 19.4)
        self.assertEqual(mathlib.add(42.123, 12.32), 54.443)
        self.assertEqual(mathlib.add(-11, 5.45), -5.55)
        self.assertEqual(mathlib.add(42.4242424242, -42.4242424242), 0)
        self.assertEqual(mathlib.add(-3.73, -21.9871474), -25.7171474)
        self.assertEqual(mathlib.add(666.666, 0), 666.666)
        self.assertEqual(mathlib.add(0, -44.9845), -44.9845)

    # Test of function sub
    def test_sub(self):

        # Integer
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

    # Test of function mul
    def test_mul(self):

        # Integer
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

    # Test of function div
    def test_div(self):

        # Cannot divide by zero.
        with self.assertRaises(ValueError):
            mathlib.div(24, 0)
        with self.assertRaises(ValueError):
            mathlib.div(-8, 0)
        with self.assertRaises(ValueError):
            mathlib.div(666.666, 0)
        with self.assertRaises(ValueError):
            mathlib.div(0, 0)

        # Integer
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

    # Test of function fac
    def test_fac(self):

        # Factorial of negative or decimal number cannot be calculated.
        with self.assertRaises(ValueError):
            mathlib.fac(-1)
        with self.assertRaises(ValueError):
            mathlib.fac(-10)
        with self.assertRaises(ValueError):
            mathlib.fac(24.24)
        with self.assertRaises(ValueError):
            mathlib.fac(-4.2)

        # Natural numbers + zero
        self.assertEqual(mathlib.fac(0), 1)
        self.assertEqual(mathlib.fac(1), 1)
        self.assertEqual(mathlib.fac(4), 24)
        self.assertEqual(mathlib.fac(10), 3628800)
        self.assertEqual(mathlib.fac(15), 1307674368000)

    # Test of function power
    def test_power(self):
        
        # Due to project specification, exponent must be natural number.
        with self.assertRaises(ValueError):
            mathlib.power(3, 0)
        with self.assertRaises(ValueError):
            mathlib.power(-576, 1.5)
        with self.assertRaises(ValueError):
            mathlib.power(24.42, -1)
        with self.assertRaises(ValueError):
            mathlib.power(16.4, -100)
        with self.assertRaises(ValueError):
            mathlib.power(0.25, -9.9)

        # Base - integer
        self.assertEqual(mathlib.power(1, 2), 1)
        self.assertEqual(mathlib.power(16, 3), 4096)
        self.assertEqual(mathlib.power(-200, 4), 1600000000)
        self.assertEqual(mathlib.power(-10, 5), -100000)
        self.assertEqual(mathlib.power(0, 9), 0)

        # Base - decimal
        self.assertEqual(mathlib.power(16.25, 3), 4291.015625)
        self.assertAlmostEqual(mathlib.power(-24.24, 4), 345247.43602, 5)
        self.assertAlmostEqual(mathlib.power(-10.1, 5), -105101.00501, 5)

    # Test of function root.
    def test_root(self):

        # In this project, root index is positive real number.
        # Root of negative number is also forbidden.
        with self.assertRaises(ValueError):
            mathlib.root(23, 0)
        with self.assertRaises(ValueError):
            mathlib.root(-4, 2)
        with self.assertRaises(ValueError):
            mathlib.root(-1000, 3)
        with self.assertRaises(ValueError):
            mathlib.root(8495, -24)
        with self.assertRaises(ValueError):
            mathlib.root(-25.5, 1.8)
        with self.assertRaises(ValueError):
            mathlib.root(567, -9.4)

        # Radicand - natural number + zero
        # Index - natural number
        self.assertEqual(mathlib.root(0, 2), 0)
        self.assertEqual(mathlib.root(1, 3), 1)
        self.assertAlmostEqual(mathlib.root(1000000, 6), 10, 1)
        self.assertAlmostEqual(mathlib.root(456445, 12), 2.962209050, 9)

        # Radicand - positive decimal number + zero
        # Index - positive decimal number
        self.assertEqual(mathlib.root(0, 3.33), 0)
        self.assertAlmostEqual(mathlib.root(2.25, 2.5), 1.383161867, 9)
        self.assertAlmostEqual(mathlib.root(4242.4242, 7.4), 3.091847895, 9)

    # Test of function log
    def test_log(self):

        # Logarithm argument must be greater than zero.
        with self.assertRaises(ValueError):
            mathlib.log(0, 10)
        with self.assertRaises(ValueError):
            mathlib.log(-1, 25.77)
        with self.assertRaises(ValueError):
            mathlib.log(-10.10, 752)

        # Logarithm base must be greater than zero and not equal to 1.
        with self.assertRaises(ValueError):
            mathlib.log(10, 0)
        with self.assertRaises(ValueError):
            mathlib.log(16.12, 1)
        with self.assertRaises(ValueError):
            mathlib.log(10, -1)
        with self.assertRaises(ValueError):
            mathlib.log(576, -42.42)

        # Argument - natural number
        # Base - natural number \ {1}
        self.assertEqual(mathlib.log(1, 10), 0)
        self.assertEqual(mathlib.log(3, 3), 1)
        self.assertAlmostEqual(mathlib.log(1000, 10), 3, 1)
        self.assertAlmostEqual(mathlib.log(455, 6), 3.41580, 5)

        # Argument - positive real number
        # Base - positive real number \ {1}
        self.assertEqual(mathlib.log(4.242, 4.242), 1)
        self.assertAlmostEqual(mathlib.log(100, 2.4), 5.26023, 5)
        self.assertAlmostEqual(mathlib.log(781.156, 7), 3.42296, 5)
        self.assertAlmostEqual(mathlib.log(156478.42, 12.12), 4.79413, 5)

    # Test of function ln.
    def test_ln(self):

        # Logarithm argument must be greater than zero.
        with self.assertRaises(ValueError):
            mathlib.ln(0)
        with self.assertRaises(ValueError):
            mathlib.ln(-1)
        with self.assertRaises(ValueError):
            mathlib.ln(-10.10)

        # Argument - natural number
        self.assertEqual(mathlib.ln(1), 0)
        self.assertAlmostEqual(mathlib.ln(100), 4.60517, 5)
        self.assertAlmostEqual(mathlib.ln(4266), 8.35843, 5)

        # Argument - positive real number
        self.assertAlmostEqual(mathlib.ln(2.7182818284), 1, 1)
        self.assertAlmostEqual(mathlib.ln(4242.4242), 8.352890, 5)


if __name__ == '__main__':
    unittest.main()
