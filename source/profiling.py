import math_lib


def sum_numbers(list_numbers):
    total = 0
    for number in list_numbers:
        total = math_lib.add(total, int(number))
    return total


def diameter(list_numbers):
    return sum_numbers(list_numbers) / len(list_numbers)


def standard_deviation(list_numbers):
    return


if __name__ == "__main__":
    string_input = input("Insert numbers for profiling (max 1000 numbers):")
    num_list = string_input.replace("\t", " ").replace("\n", " ").split(" ")
    my_diam = diameter(num_list)
    print(my_diam)
