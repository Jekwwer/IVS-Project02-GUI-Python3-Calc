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
# Function of subtracting one number from another
#
# @param a Subtrahend
# @param b Minuend
# @return Return difference between subtrahend and minuend
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
# @param a Dividend
# @param b Divisor
# @return Return quotient of dividend and divisor
def div(a, b):
    if b == 0:
        raise ValueError('Division by ZERO')
    return a / b


##
# Power function
#
# @param a Base
# @param b Exponent
# @return Return base to the power of exponent
def power(b, exp):
    if round(exp) != exp or exp <= 0:                       # According to project specification
        raise ValueError('Power must be a natural number')  # power is a natural number
    return b ** exp


##
# Function of general root
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
# Logarithm function of argument with any base
#
# @param a Argument
# @param b Base
# @return Return exponent
def log(a, b):
    if b <= 0 or b == 1 or a <= 0:
        raise ValueError

    # string variable for every digit of result exponent
    exp = ''

    # calculating with 10^-11 precision
    for i in range(12):
        # calculating nearest n power of base to argument
        n = 0
        while (b ** n) < a:
            n += 1

        if n == 0:
            nearest_power_of_b = 0
        else:
            nearest_power_of_b = n - 1

        # adding nearest powers one by one to result string
        exp += str(nearest_power_of_b)
        if i == 0:
            exp += '.'

        # calculating next argument
        a /= b ** nearest_power_of_b    # a = a / b^n
        a **= 10                        # a = a ^ 10

    return round(float(exp), 10)


##
# Natural logarithm function
#
# @param a Argument
# @return Return exponent
def ln(a):
    e = 2.718281828459045
    return log(a, e)
