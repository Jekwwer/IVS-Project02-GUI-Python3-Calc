import math_lib


def diameter(list_numbers):
    sum_numbers = 0
    for number in list_numbers:
        sum_numbers = math_lib.add(sum_numbers, int(number))
    return sum_numbers / len(list_numbers)


if __name__ == "__main__":
    string_input = input("Insert numbers for profiling (max 1000 numbers):")
    num_list = string_input.replace("\t", " ").replace("\n", " ").split(" ")
    my_diam = diameter(num_list)
    print(my_diam)
