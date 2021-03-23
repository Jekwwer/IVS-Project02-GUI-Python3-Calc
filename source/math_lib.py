# Functions for mathematical library

##
# @file math_lib.py
# @brief Functions for mathematical library
# @authors Evgenii Shiliaev  (xshili00)
#          Marko Kubrachenko (xkubra00)

##
# Function of adding two values
#
# @param a First addend
# @param b Second addend
# @return Return sum of two values
def add(a, b):
    return a + b

##
# Function to subtract one number from another
#
# @param a First number
# @param b Second number
# @return Return difference between two numbers
def sub(a, b):
    return a - b

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
