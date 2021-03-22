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
# @todo the function should be changed for x < 0 and n < 0 values
#
# @param x Radicand
# @param n index of the radical
# @return Return n-th root of radicand
def root(x, n):
    if x < 0 or n <= 0:
        raise ValueError
    return round(x ** (1 / n), 10)
