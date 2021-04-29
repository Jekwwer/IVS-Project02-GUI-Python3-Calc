#!/usr/bin/env python3

##
# @file     profiling.py
# @brief    Reads numbers and prints standard deviation
# @author   Simon Brazda (xbrazd22)
# @date     2021-04-06


import math_lib


##
# Function of sum of numbers in list
#
# @param list_numbers   List of numbers
# @return               Returns sum of numbers from the list
def sum_numbers(list_numbers):
    total = 0
    for number in list_numbers:
        total = math_lib.add(total, int(number))
    return total


##
# Function for diameter
#
# @param list_numbers   List of numbers
# @return               Returns diameter of numbers form the list
def diameter(list_numbers):
    return sum_numbers(list_numbers) / len(list_numbers)


##
# Function of standard deviation
#
# @param list_numbers   List of numbers
# @return               Returns standard deviation
def standard_deviation(list_numbers):
    a = 0
    for number in list_numbers:
        a = math_lib.add(a, math_lib.power(int(number), 2))

    b = math_lib.mul(len(list_numbers), math_lib.power(diameter(list_numbers), 2))
    s = math_lib.root(math_lib.div(math_lib.sub(a, b), math_lib.sub(len(list_numbers), 1)), 2)
    return s


if __name__ == "__main__":
    string_input = input()
    num_list = string_input.replace("\t", " ").replace("\n", " ").split(" ")
    deviation = standard_deviation(num_list)
    print(deviation)

# END OF profiling.py FILE
