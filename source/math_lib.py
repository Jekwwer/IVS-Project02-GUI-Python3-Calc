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
# Function to divide two numbers
#
# @param a First number
# @param b Second number
# @return Return result of division
def div(a, b):
    if b == 0:
        raise ValueError('Division by ZERO')
    return a / b


##
# Power function
#
# @param a Number
# @param b Power
# @return Return result of power
def power(a, b):
    if round(b) != b or b <= 0:                             # According to project specification
        raise ValueError('Power must be a natural number')  # power is a natural number
    return a ** b


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
