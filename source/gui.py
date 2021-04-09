# GIU

##
# @file    gui.py
# @brief   Graphic User Interface for the mathematical library
# @author Evgenii Shiliaev  (xshili00)

# TODO FULL EQUATOIN IN OUTPUT
# TODO UNACTIVE BUTTONS AFTER OPERATIONS
# TODO UNACTIVE BUTTIONS AFTER ERRORS

from tkinter import *
from math_lib import *

# the root of the program
root = Tk()
root.title("BHitW Calculator ")
root.geometry('272x288')
root.resizable(0, 0)

# Fields
input_field = Entry(root)
# input_field.insert(0, "Enter your expression")
input_field.grid(row=0, column=0, columnspan=3, sticky=N + S + E + W)

output_field = Label(root, bg="white", relief="sunken")
output_field.grid(row=1, column=0, columnspan=3, sticky=N + S + E + W)


# Buttons functions

##
# Function of adding button value to the input field
#
# @param num Button value
def input_button_click(value):
    current_state = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current_state) + str(value))


##
# Function of clearing the input field
def clear_button_click():
    input_field.delete(0, END)


##
# Function that calculates the expression
#
# @param operator Expression operation
# @param args Expression arguments
# @return Result of the expression
def calculate(operator, args):
    state = 0
    if operator == "+":
        result = add(args[0], args[1])
    elif operator == "-":
        result = sub(args[0], args[1])
    elif operator == "*":
        result = mul(args[0], args[1])
    elif operator == "/":
        try:
            result = div(args[0], args[1])
        except ValueError:
            result = f"Zero Division Error: {args[0]} / {args[1]} is NOT possible!"
            state = 1
    else:
        result = f"Operation Error: Used unknown operation sign!"
        state = 1
    return state, result


##
# Function that prints the result to the output field
def evaluate():
    input_str = input_field.get()
    if input_str == "":                                 # if the input field is empty
        output_str = output_field["text"]                   # get the text from output
        i = output_str.rfind("=")                           # get the index of '=' sign
        if i == -1:                                         # if there isn't
            return                                              # do nothing
        input_field.insert(0, output_str[i + 2:])           # else put the result of last operation to input field
        return                                              # end the function

    operator = "?"
    for i in range(len(input_str)):                     # find the operation sign
        if input_str[i] in ["+", "-", "/", "*"]:
            operator = input_str[i]

    if operator == "?":
        output_field.config(text="Operation Error: Used unknown operation sign!")
        return

    # get list of operands
    # TODO no .0 in integer results
    args = [float(num) for num in input_str.split(operator)]
    input_field.delete(0, END)                          # clear the input field
    exec_output, result = calculate(operator, args)     # get result
    if exec_output == 0:                                # if function ends successfully
        output_str = "{opr1} + {opr2} = {result}".format(
            opr1=args[0], opr2=args[1], result=result)
    else:
        output_str = result
    output_field.config(text=output_str)                # put the result to the output field


# NUM Buttons
num7_button = Button(root, text="7", height=2, width=4, command=lambda: input_button_click(7))
num7_button.grid(row=2, column=0)
num8_button = Button(root, text="8", height=2, width=4, command=lambda: input_button_click(8))
num8_button.grid(row=2, column=1)
num9_button = Button(root, text="9", height=2, width=4, command=lambda: input_button_click(9))
num9_button.grid(row=2, column=2)

num4_button = Button(root, text="4", height=2, width=4, command=lambda: input_button_click(4))
num4_button.grid(row=3, column=0)
num5_button = Button(root, text="5", height=2, width=4, command=lambda: input_button_click(5))
num5_button.grid(row=3, column=1)
num6_button = Button(root, text="6", height=2, width=4, command=lambda: input_button_click(6))
num6_button.grid(row=3, column=2)

num1_button = Button(root, text="1", height=2, width=4, command=lambda: input_button_click(1))
num1_button.grid(row=4, column=0)
num2_button = Button(root, text="2", height=2, width=4, command=lambda: input_button_click(2))
num2_button.grid(row=4, column=1)
num3_button = Button(root, text="3", height=2, width=4, command=lambda: input_button_click(3))
num3_button.grid(row=4, column=2)

num0_button = Button(root, text="0", height=2, width=12, command=lambda: input_button_click(0))
num0_button.grid(row=5, columnspan=2)
dec_point_button = Button(root, text=",", height=2, width=4)
dec_point_button.grid(row=5, column=2)

# Basic operation buttons
divide_button = Button(root, text="\u00F7", height=2, width=2, command=lambda: input_button_click("/"))
divide_button.grid(row=2, column=4)
multiply_button = Button(root, text="\u00D7", height=2, width=2, command=lambda: input_button_click("*"))
multiply_button.grid(row=3, column=4)
minis_button = Button(root, text="\u2212", height=2, width=2, command=lambda: input_button_click("-"))
minis_button.grid(row=4, column=4)
plus_button = Button(root, text="\u002B", height=2, width=2, command=lambda: input_button_click("+"))
plus_button.grid(row=5, column=4)

# Advanced operation buttons
nat_log_button = Button(root, text="\u33D1", height=2, width=2)
nat_log_button.grid(row=1, column=4)
log_button = Button(root, text="\u33D2", height=2, width=2)
log_button.grid(row=1, column=5)
factorial_button = Button(root, text="n!", height=2, width=2)
factorial_button.grid(row=2, column=5)
root_button = Button(root, text="\u221A", height=2, width=2)
root_button.grid(row=3, column=5)
exponent_button = Button(root, text="x\u207F", height=2, width=2)
exponent_button.grid(row=4, column=5)

# Equals button
equals_button = Button(root, text="\u003D", height=2, width=2, command=evaluate)
equals_button.grid(row=5, column=5)

# Special buttons
equals_button = Button(root, text="\u232B", height=2, width=2)
equals_button.grid(row=0, column=4)
clear_button = Button(root, text="C", height=2, width=2, command=clear_button_click)
clear_button.grid(row=0, column=5)

# MAIN loop
root.mainloop()
