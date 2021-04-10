# GIU

##
# @file    gui.py
# @brief   Graphic User Interface for the mathematical library
# @author  Evgenii Shiliaev  (xshili00)

from tkinter import *
from math_lib import *

# the root of the program
ui_root = Tk()
ui_root.title("BHitW Calculator ")
ui_root.geometry('272x288')
ui_root.resizable(0, 0)

# Fields
input_field = Entry(ui_root)
input_field.grid(row=0, column=0, columnspan=3, sticky=N + S + E + W)

output_field = Label(ui_root, bg="white", relief="sunken")
output_field.grid(row=1, column=0, columnspan=3, sticky=N + S + E + W)

# Operation list
operations_signs = ["+", "−", "/", "*", "√", "!", "^", "㏒", "㏑"]

# Functions


##
# Function of adding button value to the input field
#
# @param num Button value
def input_button_click(value):
    current_state = input_field.get()

    # Feature "Continue the calculating" (not working with logarithms)
    # If after last expression user will write an operation sign
    # Last result will copy to the input field with an operation sign
    if value in operations_signs[:-2] and current_state == "":
        input_field.insert(0, get_last_result() + str(value))
        return

    # If was added a number after an operation sign, disable the buttons
    if find_operation_sign(current_state) and value not in operations_signs:
        disable_operation_buttons()

    # Feature "Change the operation sign"
    # Before setting 2nd operand in such operations
    # User can change the operation sign by setting the other one
    # without a Backspace or Clear
    elif current_state[-1:] in operations_signs and value in operations_signs:
        current_state = current_state[:-1]
    elif current_state[-1:].isdigit() and value == "-":
        value = "−"

    # If was written decimal point, disable the decimal point button
    if value == ",":
        dec_point_button.config(state=DISABLED)

    # If was written an operation sign, enable the decimal point button
    if value in operations_signs:
        dec_point_button.config(state=NORMAL)

    # Add a value to the input field
    input_field.delete(0, END)
    input_field.insert(0, str(current_state) + str(value))


##
# Function that clears the input field
def clear_button_click():
    input_field.delete(0, END)

    # Enable disabled buttons
    dec_point_button.config(state=NORMAL)
    enable_operation_buttons()


##
# Function that deletes the last character from the input field
def backspace_button_click():
    current_state = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, current_state[:-1])

    # if last character was a decimal point, enable the decimal point button
    if current_state[-1:] == ",":
        dec_point_button.config(state=NORMAL)
    # if last character was an operation sign, enable the operation buttons
    if current_state[-1:] in operations_signs:
        enable_operation_buttons()


# Other functions

##
# Function that finds any operation sign in the string
#
# @param str_line Input string
# @return Boolean value
def find_operation_sign(str_line):
    for op in operations_signs:
        if str_line.find(op) != -1:
            return True
    return False


##
# Function that disables all operation buttons
def disable_operation_buttons():
    plus_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    root_button.config(state=DISABLED)
    factorial_button.config(state=DISABLED)
    log_button.config(state=DISABLED)
    nat_log_button.config(state=DISABLED)


##
# Function that disables all operation buttons
def enable_operation_buttons():
    plus_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    root_button.config(state=NORMAL)
    factorial_button.config(state=NORMAL)
    log_button.config(state=NORMAL)
    nat_log_button.config(state=NORMAL)


##
# Function that changes all commas in the string to dots (for mathematical operations)
#
# @param str_line Input string
# @return Modified input string
def commas_to_dots(str_line):
    for i in range(len(str_line)):
        if str_line[i] == ",":
            str_line = str_line[:i] + "." + str_line[i + 1:]
    return str_line


##
# Function that changes all dots in the string to commas (for region format)
#
# @param str_line Input string
# @return Modified input string
def dots_to_commas(str_line):
    for i in range(len(str_line)):
        if str_line[i] == ".":
            str_line = str_line[:i] + "," + str_line[i + 1:]
    return str_line


##
# Function that removes useless decimal points in integer numbers (for better appearance)
#
# @param str_line Input string
# @return Modified input string
def remove_empty_decimal_part(str_line):
    i = 0
    while str_line.find(".0", i) != -1:
        i = str_line.find(".0", i)
        # If decimal part is equal to zero, remove it
        if not str_line[i + 2:i + 3].isdigit():
            str_line = str_line[:i] + str_line[i+2:]
        i += 1
    return str_line


##
# Function that calculates the expression
#
# @param operator Expression operation
# @param args Expression arguments
# @return Result of the expression
# @exception Result ot the function execution
def calculate(operator, args):
    state = 0
    if operator == "+":
        result = add(args[0], args[1])
    elif operator == "−":
        result = sub(args[0], args[1])
    elif operator == "*":
        result = mul(args[0], args[1])
    elif operator == "/":
        try:
            result = div(args[0], args[1])
        except ValueError:
            result = f"Zero Division Error: {args[0]} / {args[1]} is NOT possible!"
            state = 1
    elif operator == "!":
        try:
            result = fac(args[0])
        except ValueError:
            result = f"Factorial Error: {args[0]} must NOT be decimal or negative!"
            state = 1
    elif operator == "^":
        try:
            result = power(args[0], args[1])
        except ValueError:
            result = f"Power Error: {args[1]} MUST be a natural number!"
            state = 1
    elif operator == "√":
        try:
            result = root(args[1], args[0])
        except ValueError:
            result = "Nth Root Error: Invalid arguments\n" \
                     "Check 'Help' or 'User Manual' for more information"
            state = 1
    elif operator == "㏑":
        try:
            result = ln(args[0])
        except ValueError:
            result = f"Natural Logarithm Error: {args[0]} MUST be greater than zero."
            state = 1
    elif operator == "㏒":
        try:
            result = log(args[1], args[0])
        except ValueError:
            result = "Logarithm Error: Invalid arguments\n" \
                     "Check 'Help' or 'User Manual' for more information"
            state = 1
    else:
        result = f"Operation Error: Used unknown operation sign!"
        state = 1
    return state, result


##
# Function preparing the output string for output field
#
# @param operator Expression operation
# @param args Expression arguments
# @param result Expression result
# @return String of the equation
def get_output_str(operator, args, result):
    output_str = ""

    # Check numbers negativity
    if args[0] < 0:
        args[0] = f"({args[0]})"
    if result < 0:
        result = f"({result})"

    if len(args) == 2:
        if args[1] < 0:
            args[1] = f"({args[1]})"

        if operator == "^" or operator == "㏒":
            output_str = "{opr1}{operator}{opr2} = {result}".format(
                opr1=args[0], opr2=args[1], operator=operator, result=result)
        elif operator == "−":
            output_str = "{opr1} {operator} {opr2} = {result}".format(
                opr1=args[0], opr2=args[1], operator=operator, result=result)
        else:
            output_str = "{opr1} {operator} {opr2} = {result}".format(
                opr1=args[0], opr2=args[1], operator=operator, result=result)

    elif len(args) == 1:
        if operator == "㏑":
            output_str = "{operator}({opr1}) = {result}".format(
                opr1=args[0], operator=operator, result=result)
        else:
            output_str = "{opr1}{operator} = {result}".format(
                opr1=args[0], operator=operator, result=result)

    return output_str


##
# Function preparing the output string for output field
#
# @return Result of the last expression or an empty string
def get_last_result():
    output_str = output_field["text"]       # get the text from output
    i = output_str.rfind("=")               # get the index of '=' sign
    if i == -1:                             # if there isn't
        return ""                           # return nothing
    else:
        return remove_parentheses(output_str[i+1:])


##
# Function that removes parentheses in string
#
# @param str_line Input string
# @return Modified input string
def remove_parentheses(str_line):
    for p in "()":
        i = 0
        while str_line.find(p, i) != -1:
            i = str_line.find(p, i)
            if i > 0:
                str_line = str_line[:i] + str_line[i + 1:]
            i += 1
    return str_line


##
# Function that prints the result to the output field
def evaluate():
    input_str = commas_to_dots(input_field.get())

    # Feature "Get last result" (not working with basic logarithm properly)
    # If after last expression user will write an equation sign again
    # Last result will copy to the input field
    if input_str == "":                                 # if the input field is empty
        input_field.insert(0, get_last_result())        # put the result of last operation to input field
        return                                          # end the function

    # Default values
    operator = "?"
    args = []  # TODO INVALID OPERANDS

    # Find the operation sign and set the arguments
    for i in range(len(input_str)):
        if input_str[i] in ["+", "−", "/", "*", "√", "^", "㏒"]:
            operator = input_str[i]
            args = [float(num) for num in input_str.split(operator)]
            break
        elif input_str[i] in ["!", "㏑"]:
            operator = input_str[i]
            num = float(input_str.replace(operator, ""))
            args = [num]
            break

    if operator == "?":                                 # if the operation sign hadn't been changed
        output_field.config(text="Operation Error: Used unknown operation sign!")
        return

    exec_output, result = calculate(operator, args)     # get result
    if exec_output == 0:                                # if function ends successfully
        input_field.delete(0, END)                      # clear the input field
        output_str = get_output_str(operator, args, result)
    else:
        output_str = result                             # else put error message to the

    output_str = remove_empty_decimal_part(output_str)  # Remove useless decimal parts
    output_str = dots_to_commas(output_str)             # Replace dots with commas
    output_field.config(text=output_str)                # put the result to the output field
    enable_operation_buttons()


# NUM Buttons
num7_button = Button(ui_root, text="7", height=2, width=4, command=lambda: input_button_click(7))
num7_button.grid(row=2, column=0)
num8_button = Button(ui_root, text="8", height=2, width=4, command=lambda: input_button_click(8))
num8_button.grid(row=2, column=1)
num9_button = Button(ui_root, text="9", height=2, width=4, command=lambda: input_button_click(9))
num9_button.grid(row=2, column=2)

num4_button = Button(ui_root, text="4", height=2, width=4, command=lambda: input_button_click(4))
num4_button.grid(row=3, column=0)
num5_button = Button(ui_root, text="5", height=2, width=4, command=lambda: input_button_click(5))
num5_button.grid(row=3, column=1)
num6_button = Button(ui_root, text="6", height=2, width=4, command=lambda: input_button_click(6))
num6_button.grid(row=3, column=2)

num1_button = Button(ui_root, text="1", height=2, width=4, command=lambda: input_button_click(1))
num1_button.grid(row=4, column=0)
num2_button = Button(ui_root, text="2", height=2, width=4, command=lambda: input_button_click(2))
num2_button.grid(row=4, column=1)
num3_button = Button(ui_root, text="3", height=2, width=4, command=lambda: input_button_click(3))
num3_button.grid(row=4, column=2)

num0_button = Button(ui_root, text="0", height=2, width=12, command=lambda: input_button_click(0))
num0_button.grid(row=5, columnspan=2)
dec_point_button = Button(ui_root, text=",", height=2, width=4, command=lambda: input_button_click(","))
dec_point_button.grid(row=5, column=2)

# Basic operation buttons
divide_button = Button(ui_root, text="÷", height=2, width=2, command=lambda: input_button_click("/"))
divide_button.grid(row=2, column=4)
multiply_button = Button(ui_root, text="×", height=2, width=2, command=lambda: input_button_click("*"))
multiply_button.grid(row=3, column=4)
minis_button = Button(ui_root, text="−", height=2, width=2, command=lambda: input_button_click("-"))
minis_button.grid(row=4, column=4)
plus_button = Button(ui_root, text="+", height=2, width=2, command=lambda: input_button_click("+"))
plus_button.grid(row=5, column=4)

# Advanced operation buttons
nat_log_button = Button(ui_root, text="㏑", height=2, width=2, command=lambda: input_button_click("㏑"))
nat_log_button.grid(row=1, column=4)
log_button = Button(ui_root, text="㏒", height=2, width=2, command=lambda: input_button_click("㏒"))
log_button.grid(row=1, column=5)
factorial_button = Button(ui_root, text="n!", height=2, width=2, command=lambda: input_button_click("!"))
factorial_button.grid(row=2, column=5)
root_button = Button(ui_root, text="√", height=2, width=2, command=lambda: input_button_click("√"))
root_button.grid(row=3, column=5)
exponent_button = Button(ui_root, text="xⁿ", height=2, width=2, command=lambda: input_button_click("^"))
exponent_button.grid(row=4, column=5)

# Equals button
equals_button = Button(ui_root, text="=", height=2, width=2, command=evaluate)
equals_button.grid(row=5, column=5)

# Special buttons
backspace_button = Button(ui_root, text="⌫", height=2, width=2, command=backspace_button_click)
backspace_button.grid(row=0, column=4)
clear_button = Button(ui_root, text="C", height=2, width=2, command=clear_button_click)
clear_button.grid(row=0, column=5)

# MAIN loop
ui_root.mainloop()
