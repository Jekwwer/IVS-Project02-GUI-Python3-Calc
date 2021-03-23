# Functions for mathematical library

##
# @file math_lib.py
# @brief Functions for mathematical library
# @author Evgenii Shiliaev (xshili00)

##
# Function of adding two values
#
# @param a First addend
# @param b Second addend
# @return Return sum of two values
def add(a, b):
    return a + b


##
# Function of multiplying two values
#
# @param a First factor
# @param b Second factor
# @return Return product of two values
def mul(a, b):
    return a * b


##
# Function of general root two values
#
# @param x Radicand
# @param n index of the radical
# @return Return n-th root of radicand
def root(x, n):
    if n == 0:
        raise ValueError
    # if radicand is less than zero and index is even
    elif x < 0 and n % 2 == 0:
        raise ValueError
    # if radicand is less than zero and index is decimal
    elif x < 0 and n - int(n) != 0 and int(n * 10) % 10 != 0:
        raise ValueError

    if x < 0:
        return -((-x) ** (1 / n))
    else:
        return x ** (1 / n)


##
# Function of logarithm
#
# @todo the function should be changed for non-natural numbers
#
# @param a Argument
# @param b Base
# @return Return exponent
def log(a, b):
    if b <= 0 or b == 1 or a <= 0:
        raise ValueError

    e = 0
    while a > 1:
        e += 1
        a //= b

    return e
