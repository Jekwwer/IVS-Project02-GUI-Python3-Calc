# GIU

##
# @file    gui.py
# @brief   Graphic User Interface for the mathematical library
# @authors Evgenii Shiliaev  (xshili00)
#          Marko Kubrachenko (xkubra00)
#          Pavel Beneš       (xbenes58)

from tkinter import *
from math_lib import *

# TODO MAKE APP WINDOWS RESIZABLE WITH THE TEXT IN IT

# the root of the program
ui_root = Tk()
ui_root.title("BHitW Calculator ")
ui_root.resizable(0, 0)
ui_root.geometry("350x360")
ui_root.minsize(350, 360)


##
# Function to open 'About' window
def open_about_window():
    new_window = Toplevel(ui_root)
    new_window.title("About")
    new_window.geometry("350x360")
    new_window.minsize(350, 360)
    new_window.resizable(0, 0)
    Label(new_window, text="This calculator application was created as the 2nd project "
                           "of the \"Practical Aspects of Software Design\" subject "
                           "by the team \"Blue Hair is the Way\""
                           "\n", wraplength=340, justify='left').grid(row=0)

    Label(new_window, text="Authors:\n"
                           "• xshili00 Evgenii Shiliaev\n"
                           "• xbenes58 Pavel Beneš\n"
                           "• xkubra00 Marko Kubrachenko\n"
                           "• xbrazd22 Šimon Brázda", font="Courier", wraplength=340, justify='left').grid(
        row=1)


##
# Function to open Help window
def open_help_window():
    new_window = Toplevel(ui_root)
    new_window.title("Help")
    new_window.geometry("350x360")
    new_window.minsize(350, 360)
    Label(new_window, text="This is a help window").pack()


# Menu
main_menu = Menu(ui_root, bg='#003d63', fg='#ffffff', activebackground='#195e89',
                 activeforeground='#ffffff')
ui_root.config(menu=main_menu)
main_menu.add_command(label='About', font="Arial", command=open_about_window)
main_menu.add_command(label='Help', font="Arial", command=open_help_window)

# Fields
input_field = Label(ui_root, borderwidth=1, bg='#dedede', relief=SOLID, font=("Arial", 18), wraplength=225,
                    justify="center")
input_field.place(relheight=0.2, relwidth=0.75, relx=0, rely=0)

output_field = Label(ui_root, borderwidth=1, bg="#dedede", relief=SOLID, font=("Arial", 14), wraplength=225,
                     justify="center")
output_field.place(relheight=0.2, relwidth=0.75, relx=0, rely=0.2)

# Operation list
operations_signs = ["+", "−", "/", "*", "√", "!", "^", "㏒", "㏑"]


# Functions

##
# Function of adding button value to the input field
#
# @param num Button value
def input_button_click(value):
    if not check_num_availability(value):
        return
    current_state = input_field["text"]
    # current_state = input_field.get()

    # Feature "Continue the calculating" (not working with logarithms)
    # If after last expression user will write an operation sign
    # Last result will copy to the input field with an operation sign
    if value in operations_signs[:-2] and current_state == "":
        input_field.config(text=get_last_result() + str(value))
        # input_field.insert(0, get_last_result() + str(value))
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

    # If was written a number, disable a natural logarithm button
    if str(value).isdigit():
        nat_log_button.config(state=DISABLED)

    # If the value is digit or minus sigh and there is an operation sign in the input field
    if (str(value).isdigit() or value == "-") and current_state[-1:] in operations_signs:
        minis_button.config(state=DISABLED)

    # If was written an operation sign, enable the decimal point button
    if value in operations_signs:
        dec_point_button.config(state=NORMAL)

    # Add a value to the input field
    input_field.config(text=str(current_state) + str(value))
    # input_field.delete(0, END)
    # input_field.insert(0, str(current_state) + str(value))


##
# Function that clears the input field
def clear_button_click(event=None):
    input_field.config(text="")
    # input_field.delete(0, END)

    # Enable disabled buttons
    dec_point_button.config(state=NORMAL)
    minis_button.config(state=NORMAL)
    enable_operation_buttons()


##
# Function that deletes the last character from the input field
def backspace_button_click(event=None):
    current_state = input_field["text"]
    # current_state = input_field.get()
    # input_field.delete(0, END)
    input_field.config(text=current_state[:-1])
    # input_field.insert(0, current_state[:-1])

    # if last character was a decimal point, enable the decimal point button
    if current_state[-1:] == ",":
        dec_point_button.config(state=NORMAL)
    # if last character was an operation sign, enable the operation buttons
    if current_state[-2:-1] in operations_signs or current_state[-1:] in operations_signs:
        enable_operation_buttons()
        minis_button.config(state=NORMAL)
    if current_state[:-1] == "":
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
# Function that checks buttons availability for correct keyboard input
#
# @param value Button input value
# @return Boolean value
def check_num_availability(value):
    if value == "+" and plus_button["state"] == tkinter.DISABLED:
        return False
    if value == "-" and minis_button["state"] == tkinter.DISABLED:
        return False
    if value == "*" and multiply_button["state"] == tkinter.DISABLED:
        return False
    if value == "/" and divide_button["state"] == tkinter.DISABLED:
        return False
    if value == "√" and root_button["state"] == tkinter.DISABLED:
        return False
    if value == "!" and factorial_button["state"] == tkinter.DISABLED:
        return False
    if value == "^" and exponent_button["state"] == tkinter.DISABLED:
        return False
    if value == "㏒" and log_button["state"] == tkinter.DISABLED:
        return False
    if value == "㏑" and nat_log_button["state"] == tkinter.DISABLED:
        return False
    if value == "," and dec_point_button["state"] == tkinter.DISABLED:
        return False

    return True


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
            str_line = str_line[:i] + str_line[i + 2:]
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
                     "Check 'Help' or 'User Manual' for more information."
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
                     "Check 'Help' or 'User Manual' for more information."
            state = 1
    else:
        result = "Operation Error:\n" \
                 "Used unknown operation sign!"
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

        if operator == "^" or operator == "㏒" or operator == "√":
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
        return remove_parentheses(output_str[i + 1:])


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
def evaluate(event=None):
    input_str = commas_to_dots(input_field["text"])
    # input_str = commas_to_dots(input_field.get())

    # Feature "Get last result" (not working with basic logarithm properly)
    # If after last expression user will write an equation sign again
    # Last result will copy to the input field
    if input_str == "":
        input_field.config(text=get_last_result())
        # input_field.insert(0, get_last_result())        # put the result of last operation to input field
        return

    # Default values
    operator = "?"
    args = []  # TODO INVALID OPERANDS

    # Find the operation sign and set the arguments
    for i in range(len(input_str)):
        if input_str[i] in ["+", "−", "/", "*", "√", "^", "㏒"]:
            operator = input_str[i]
            # if radical index wasn't set
            if operator == "√" and not input_str[:1].isdigit():
                input_str = "2" + input_str
            if operator == "+":
                operator_index = input_str.rfind("+")
                args.append(float(input_str[:operator_index]))
                args.append(float(input_str[operator_index + 1:]))
                break
            args = [float(num) for num in input_str.split(operator)]
            break
        elif input_str[i] in ["!", "㏑"]:
            operator = input_str[i]
            num = float(input_str.replace(operator, ""))
            args = [num]
            break

    # if the operation sign hadn't been changed
    if operator == "?":
        output_field.config(text="Operation Error:\nUsed unknown operation sign!")
        return

    exec_output, result = calculate(operator, args)     # get result
    if exec_output == 0:                                # if function ends successfully
        input_field.config(text="")
        # input_field.delete(0, END)                      # clear the input field
        output_str = get_output_str(operator, args, result)
    else:
        output_str = result                             # else put error message to the

    output_str = remove_empty_decimal_part(output_str)  # Remove useless decimal parts
    output_str = dots_to_commas(output_str)             # Replace dots with commas
    output_field.config(text=output_str)                # put the result to the output field
    enable_operation_buttons()
    minis_button.config(state=NORMAL)
    dec_point_button.config(state=NORMAL)


# Definition of buttons and binding keys

# NUM Buttons
num7_button = Button(ui_root, text="7", command=lambda: input_button_click(7))
num7_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num7_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.4)

ui_root.bind("<Key-7>", lambda value: input_button_click(7))
ui_root.bind("<KP_7>", lambda value: input_button_click(7))

num8_button = Button(ui_root, text="8", command=lambda: input_button_click(8))
num8_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num8_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.4)

ui_root.bind("<Key-8>", lambda value: input_button_click(8))
ui_root.bind("<KP_8>", lambda value: input_button_click(8))

num9_button = Button(ui_root, text="9", command=lambda: input_button_click(9))
num9_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num9_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.4)

ui_root.bind("<Key-9>", lambda value: input_button_click(9))
ui_root.bind("<KP_9>", lambda value: input_button_click(9))

num4_button = Button(ui_root, text="4", command=lambda: input_button_click(4))
num4_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num4_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.55)

ui_root.bind("<Key-4>", lambda value: input_button_click(4))
ui_root.bind("<KP_4>", lambda value: input_button_click(4))

num5_button = Button(ui_root, text="5", command=lambda: input_button_click(5))
num5_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num5_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.55)

ui_root.bind("<Key-5>", lambda value: input_button_click(5))
ui_root.bind("<KP_5>", lambda value: input_button_click(5))

num6_button = Button(ui_root, text="6", command=lambda: input_button_click(6))
num6_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num6_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.55)

ui_root.bind("<Key-6>", lambda value: input_button_click(6))
ui_root.bind("<KP_6>", lambda value: input_button_click(6))

num1_button = Button(ui_root, text="1", command=lambda: input_button_click(1))
num1_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num1_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.7)

ui_root.bind("<Key-1>", lambda value: input_button_click(1))
ui_root.bind("<KP_1>", lambda value: input_button_click(1))

num2_button = Button(ui_root, text="2", command=lambda: input_button_click(2))
num2_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num2_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.7)

ui_root.bind("<Key-2>", lambda value: input_button_click(2))
ui_root.bind("<KP_2>", lambda value: input_button_click(2))

num3_button = Button(ui_root, text="3", command=lambda: input_button_click(3))
num3_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num3_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.7)

ui_root.bind("<Key-3>", lambda value: input_button_click(3))
ui_root.bind("<KP_3>", lambda value: input_button_click(3))

num0_button = Button(ui_root, text="0", command=lambda: input_button_click(0))
num0_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
num0_button.place(relheight=0.15, relwidth=0.5, relx=0, rely=0.85)

ui_root.bind("<Key-0>", lambda value: input_button_click(0))
ui_root.bind("<KP_0>", lambda value: input_button_click(0))

dec_point_button = Button(ui_root, text=",", command=lambda: input_button_click(","))
dec_point_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                        fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
dec_point_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.85)

ui_root.bind("<Key-comma>", lambda value: input_button_click(","))
ui_root.bind("<KP_Decimal>", lambda value: input_button_click(","))

# Basic operation buttons
divide_button = Button(ui_root, text="÷", command=lambda: input_button_click("/"))
divide_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                     fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
divide_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.4)

ui_root.bind("<Key-slash>", lambda value: input_button_click("/"))
ui_root.bind("<KP_Divide>", lambda value: input_button_click("/"))

multiply_button = Button(ui_root, text="×", command=lambda: input_button_click("*"))
multiply_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                       fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
multiply_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.55)

ui_root.bind("<Key-asterisk>", lambda value: input_button_click("*"))
ui_root.bind("<KP_Multiply>", lambda value: input_button_click("*"))

minis_button = Button(ui_root, text="−", command=lambda: input_button_click("-"))
minis_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                    fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
minis_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.7)

ui_root.bind("<Key-minus>", lambda value: input_button_click("-"))
ui_root.bind("<KP_Subtract>", lambda value: input_button_click("-"))

plus_button = Button(ui_root, text="+", command=lambda: input_button_click("+"))
plus_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
plus_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.85)

ui_root.bind("<Key-plus>", lambda value: input_button_click("+"))
ui_root.bind("<KP_Add>", lambda value: input_button_click("+"))

# Advanced operation buttons
nat_log_button = Button(ui_root, text="㏑", command=lambda: input_button_click("㏑"))
nat_log_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                      fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
nat_log_button.place(relheight=0.2, relwidth=0.125, relx=0.75, rely=0.2)

ui_root.bind("<Key-n>", lambda value: input_button_click("㏑"))
ui_root.bind("<Key-N>", lambda value: input_button_click("㏑"))

log_button = Button(ui_root, text="㏒", command=lambda: input_button_click("㏒"))
log_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                  fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
log_button.place(relheight=0.2, relwidth=0.125, relx=0.875, rely=0.2)

ui_root.bind("<Key-l>", lambda value: input_button_click("㏒"))
ui_root.bind("<Key-L>", lambda value: input_button_click("㏒"))

factorial_button = Button(ui_root, text="n!", command=lambda: input_button_click("!"))
factorial_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                        fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
factorial_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.4)

ui_root.bind("<Key-exclam>", lambda value: input_button_click("!"))

root_button = Button(ui_root, text="√", command=lambda: input_button_click("√"))
root_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                   fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
root_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.55)

ui_root.bind("<Key-r>", lambda value: input_button_click("√"))
ui_root.bind("<Key-R>", lambda value: input_button_click("√"))

exponent_button = Button(ui_root, text="xⁿ", command=lambda: input_button_click("^"))
exponent_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                       fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
exponent_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.7)

ui_root.bind("<Key-asciicircum>", lambda value: input_button_click("^"))

# Equals button
equals_button = Button(ui_root, text="=", command=evaluate)
equals_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                     fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
equals_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.85)

ui_root.bind("<Return>", evaluate)
ui_root.bind("<KP_Enter>", evaluate)
ui_root.bind("<Key-equal>", evaluate)

# Special buttons
backspace_button = Button(ui_root, text="⌫", command=backspace_button_click)
backspace_button.config(relief=FLAT, font=("Arial", 18, "bold"), bg='#003d63', activebackground='#195e89',
                        fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
backspace_button.place(relheight=0.2, relwidth=0.125, relx=0.75, rely=0)

ui_root.bind("<Key-BackSpace>", backspace_button_click)
ui_root.bind("<Key-Delete>", backspace_button_click)

clear_button = Button(ui_root, text="C", command=clear_button_click)
clear_button.config(relief=FLAT, font=("Arial", 20, "bold"), bg='#003d63', activebackground='#195e89',
                    fg='#ffffff', activeforeground='#ffffff', highlightbackground='black')
clear_button.place(relheight=0.2, relwidth=0.125, relx=0.875, rely=0)

ui_root.bind("<Key-c>", clear_button_click)
ui_root.bind("<Key-C>", clear_button_click)

# MAIN loop
ui_root.mainloop()
