# Functions for mathematical library

##
# @file    math_lib.py
# @brief   Functions for mathematical library
# @authors Evgenii Shiliaev  (xshili00)
# @authors Marko Kubrachenko (xkubra00)

##
# Function of adding two values
#
# @param a First addend
# @param b Second addend
# @return  Returns sum of two values
def add(a, b):
    return a + b


##
# Function of subtracting one number from another
#
# @param a Subtrahend
# @param b Minuend
# @return  Returns difference between subtrahend and minuend
def sub(a, b):
    return a - b


##
# Function of multiplying two values
#
# @param a Multiplicand
# @param b Multiplier
# @return  Returns product of two values
def mul(a, b):
    return round((a * b), 10)


##
# Function to divide two numbers
#
# @param a Dividend
# @param b Divisor
# @return  Returns quotient of dividend and divisor
def div(a, b):
    # Division by zero
    if b == 0:
        raise ValueError
    return round((a / b), 10)


##
# Power function
#
# @param b   Base
# @param exp Exponent
# @return    Returns base to the power of exponent
def power(b, exp):
    # According to project specification power is a natural number
    if round(exp) != exp or exp <= 0:
        raise ValueError
    return round((b ** exp), 10)


##
# Factorial function
#
# @param a Number
# @return  Returns factorial of entered number
def fac(a):
    # Factorial does not exist for negative or decimal numbers
    if round(a) != a or a < 0:
        raise ValueError
    a = int(a)
    factorial = 1
    # Factorial of 1 is 0
    if a == 0:
        return factorial
    else:
        for i in range(1, a + 1):
            factorial = factorial * i
    return factorial


##
# Function of general root
#
# @param x Radicand
# @param n Index of the radical
# @return  Returns n-th root of radicand
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
# @return  Returns exponent
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
# @return  Returns exponent
def ln(a):
    e = 2.718281828459045
    return log(a, e)
