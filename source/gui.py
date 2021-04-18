# GIU

##
# @file    gui.py
# @brief   Graphic User Interface for the mathematical library
# @authors Evgenii Shiliaev  (xshili00)
#          Marko Kubrachenko (xkubra00)
#          Pavel Beneš       (xbenes58)

from tkinter import *
from tkinter import ttk
from math_lib import *

# The root of the program
master = Tk()

# Main window
master.title("BHitW Calculator ")
master.resizable(False, False)
min_window_width = 350
min_window_height = 370

# Upper center screen coordinates
x_position = int(master.winfo_screenwidth() / 2 - min_window_width / 2)
y_position = int(master.winfo_screenheight() / 3 - min_window_height / 2)

# Put thw  main window to the (x,y)
master.geometry(f"{min_window_width}x{min_window_height}+{x_position}+{y_position}")
master.minsize(min_window_width, min_window_height)

# Menu
main_menu = Menu(master, bg="#003d63", fg="#ffffff", activebackground="#195e89",
                 activeforeground="#ffffff")
master.config(menu=main_menu)


##
# Function that opens Help window
def open_help_window():
    global help_window
    # If the window is opened, focus on it
    try:
        if help_window.state() == "normal":
            help_window.focus()
    # Else open it
    except (NameError, TclError):
        help_window = HelpWindow(master)


main_menu.add_command(label="Help", font="Arial", command=open_help_window)

##
# Function that opens About window
def open_about_window():
    global about_window
    # If the window is opened, focus on it
    try:
        if about_window.state() == "normal":
            about_window.focus()
    # Else open it
    except (NameError, TclError):
        about_window = AboutWindow(master)


main_menu.add_command(label="About", font="Arial", command=open_about_window)

# Fields
default_wraplength = 235
default_input_font_size = 18
input_field = Label(master, borderwidth=1, bg="#dadada", relief=SOLID, font=("Arial", default_input_font_size),
                    wraplength=default_wraplength,
                    justify="center")
input_field.place(relheight=0.18, relwidth=0.75, relx=0, rely=0)

default_output_font_size = 14
output_field = Label(master, borderwidth=1, bg="#dadada", relief=SOLID, font=("Arial", default_output_font_size),
                     wraplength=default_wraplength,
                     justify="center")
output_field.place(relheight=0.18, relwidth=0.75, relx=0, rely=0.18)

# Frame
frame = Frame(master, bg="#dadada", highlightbackground="black")
frame.pack(side="bottom", fill=X)

# Sizegrip
ttk.Style().layout("Sizer.TLabel", [("Sizegrip.sizegrip",
                                     {"sticky": "se", "side": "bottom"})])
sizegrip = ttk.Label(frame, style="Sizer.TLabel")
sizegrip.pack(anchor="se")

# Operation list
operations_signs = ["+", "−", "/", "*", "!", "^", "√", "㏒", "㏑"]


# Additional windows

##
# Class of the About window
class AboutWindow(Toplevel):
    ##
    # Function that inisializes the About window
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("About")

        # Put on the Left upper center part of the screen
        x_position = int(master.winfo_screenwidth() / 2 + min_window_width / 2)
        y_position = int(master.winfo_screenheight() / 3 - min_window_height / 2)
        self.geometry(f"{min_window_width}x{min_window_height}+{x_position}+{y_position}")
        self.minsize(min_window_width, min_window_height)
        self.resizable(0, 0)

        # About window frame
        about_win_frame = Frame(self, bg="#dadada", highlightbackground="black")
        about_win_frame.pack(side="bottom", fill=X)

        # About window sizegrip
        ttk.Style().layout("Sizer.TLabel", [("Sizegrip.sizegrip",
                                             {"sticky": "se", "side": "bottom"})])
        about_win_sizegrip = ttk.Label(about_win_frame, style="Sizer.TLabel")
        about_win_sizegrip.pack(anchor="se")

        about_win_sizegrip.bind("<ButtonPress-1>", sizegrip_button_press)
        about_win_sizegrip.bind("<B1-Motion>", lambda value: resize_additional_window(value, self,
                                                                                      [app_about_label, authors_label],
                                                                                      default_font_size))
        about_win_sizegrip.bind("<ButtonRelease-1>", sizegrip_button_release)

        # Put some labels
        default_font_size = 13
        app_about_label = Label(self, text="This calculator application was created as the 2nd project "
                                           "of the \"Practical Aspects of Software Design\" subject "
                                           "by the team \"Blue Hair is the Way\n", font=("Arial", default_font_size),
                                wraplength=min_window_width,
                                justify="left")
        app_about_label.pack()

        authors_label = Label(self, text="Authors:\n"
                                         "• xshili00 Evgenii Shiliaev\n"
                                         "• xbenes58 Pavel Beneš\n"
                                         "• xkubra00 Marko Kubrachenko\n"
                                         "• xbrazd22 Šimon Brázda", font=("Courier", default_font_size),
                              wraplength=min_window_width,
                              justify="left")
        authors_label.pack()

        # Exit About window shortcut
        self.bind("<Escape>", lambda value: self.destroy())


##
# Class of the Help window
class HelpWindow(Toplevel):
    ##
    # Function that inisializes the Help window
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Help")

        # Put on the Left upper center part of the screen
        x_position = int(master.winfo_screenwidth() / 2 + min_window_width / 2)
        y_position = int(master.winfo_screenheight() / 3 - min_window_height / 2)
        self.geometry(f"{min_window_width}x{min_window_height}+{x_position}+{y_position}")
        self.minsize(min_window_width, min_window_height)
        self.resizable(0, 0)

        # Help window frame
        help_window_frame = Frame(self, bg="#dadada", highlightbackground="black")
        help_window_frame.pack(side="bottom", fill=X)

        # Help window sizegrip
        ttk.Style().layout("Sizer.TLabel", [("Sizegrip.sizegrip",
                                             {"sticky": "se", "side": "bottom"})])
        about_win_sizegrip = ttk.Label(help_window_frame, style="Sizer.TLabel")
        about_win_sizegrip.pack(anchor="se")

        about_win_sizegrip.bind("<ButtonPress-1>", sizegrip_button_press)
        about_win_sizegrip.bind("<B1-Motion>", lambda value: resize_additional_window(value, self, [help_label],
                                                                                      default_font_size))
        about_win_sizegrip.bind("<ButtonRelease-1>", sizegrip_button_release)

        # Put some labels
        default_font_size = 13
        help_label = Label(self, text="This is a help window", font=("Arial", default_font_size))
        help_label.pack()

        # Exit Help window shortcut
        self.bind("<Escape>", lambda value: self.destroy())


# Help hotkeys
master.bind("<H>", lambda value: open_help_window())
master.bind("<h>", lambda value: open_help_window())


# Functions

##
# Function of adding button value to the input field
#
# @param value Button value
def input_button_press(value):
    # If button is disabled (for keyboard input)
    if not check_num_availability(value):
        return

    # Get string from the input
    input_str = input_field["text"]

    # Feature "Continue the calculating" (not working with logarithms and root)
    # If after the last expression user will write an operation sign,
    # last result will copy to the input field with an operation sign
    if value in operations_signs[:-3] and input_str == "":
        input_field.config(text=get_last_result() + str(value))
        return
    # (for correct minus sign working)
    elif value == "-" and input_str == "" and output_field["text"] != "":
        input_field.config(text=get_last_result() + "−")
        return

    # If was added a number after an operation sign, disable the buttons
    if find_operation_sign(input_str) and value not in operations_signs:
        disable_operation_buttons()

    # Feature "Change the operation sign"
    # Before setting 2nd operand in such operations
    # user can change the operation sign by setting the other one
    # without a Backspace or Clear button call
    if input_str[-1:] in operations_signs and value in operations_signs:
        input_str = input_str[:-1]
    if input_str[-1:].isdigit() and value == "-":
        value = "−"

    # If was written decimal point, disable the decimal point button
    if value == ",":
        dec_point_button.config(state=DISABLED)

    # If was written a number, disable a natural logarithm button
    # (natural logarithm get arguments only after itself)
    if str(value).isdigit():
        nat_log_button.config(state=DISABLED)

    # If the value is digit or minus sigh and there is an operation sign in the input field
    # disable the minus button
    if (str(value).isdigit() or value == "-") and input_str[-1:] in operations_signs:
        minis_button.config(state=DISABLED)

    # If was written an operation sign, enable the decimal point button
    if value in operations_signs:
        dec_point_button.config(state=NORMAL)

    # Add a value to the input field
    input_field.config(text=str(input_str) + str(value))


##
# Function that clears the input field
def clear_button_click(event=None):
    input_field.config(text="")

    # Enable disabled buttons
    dec_point_button.config(state=NORMAL)
    minis_button.config(state=NORMAL)
    enable_operation_buttons()


##
# Function that deletes the last character from the input field
def backspace_button_click(event=None):
    input_str = input_field["text"]
    input_field.config(text=input_str[:-1])
    # If last character was a decimal point, enable the decimal point button
    if input_str[-1:] == ",":
        dec_point_button.config(state=NORMAL)
    # If last character was an operation sign, enable the operation buttons
    if input_str[-2:-1] in operations_signs or input_str[-1:] in operations_signs:
        enable_operation_buttons()
        minis_button.config(state=NORMAL)
    # If input field is empty
    if input_str[:-1] == "":
        enable_operation_buttons()


##
# Function that catches pressing the sizegrip button
def sizegrip_button_press(event):
    sizegrip["cursor"] = "bottom_right_corner"


def resize_additional_window(event, window, labels, default_font_size):
    delta_x = event.x_root - window.winfo_rootx()
    delta_y = event.y_root - window.winfo_rooty()

    if delta_x < 1:
        delta_x = 1
    if delta_y < 1:
        delta_y = 1
    window.geometry("%sx%s" % (delta_x, delta_y))

    for i in range(len(labels)):
        label_font_config = (labels[i]["font"].split())[0]
        label_font_size = default_font_size
        if delta_x >= min_window_width:
            label_font_size = int(delta_x / min_window_width * default_font_size)
        labels[i].config(font=(label_font_config[0], label_font_size))
        if delta_x < min_window_width:
            delta_x = min_window_width
        labels[i].config(wraplength=delta_x - 10)


##
# Function that resizes the main app window
def resize_main_window(event):
    delta_x = event.x_root - master.winfo_rootx()
    delta_y = event.y_root - master.winfo_rooty()

    num_buttons_text_size = other_buttons_text_size = default_button_text_size

    if delta_x / 16 > delta_y / 9:
        if delta_x >= min_window_width:
            num_buttons_text_size = delta_x / 17.5
            other_buttons_text_size = delta_x / 17.5
        if delta_x >= 500:
            num_buttons_text_size = delta_x / 17.5 - delta_x / 100
            other_buttons_text_size = delta_x / 17.5 - delta_x / 100
        if delta_x >= 950:
            num_buttons_text_size = delta_x / 17.5 - delta_x / 100 - delta_x / 85
            other_buttons_text_size = delta_x / 17.5 - delta_x / 100 - delta_x / 85
        if delta_x >= 1600:
            num_buttons_text_size = delta_x / 17.5 - delta_x / 100 - delta_x / 85 - delta_x / 125
            other_buttons_text_size = delta_x / 17.5 - delta_x / 100 - delta_x / 85 - delta_x / 125

    else:
        if delta_y >= min_window_height:
            num_buttons_text_size = delta_y / 18
            other_buttons_text_size = delta_y / 18
        if delta_y >= 540 and delta_x < 400:
            other_buttons_text_size = delta_y / 20
        if delta_y >= 600 and delta_x < 1000:
            other_buttons_text_size = delta_y / 22
        if delta_y >= 700 and delta_x < 900:
            other_buttons_text_size = delta_y / 25
        if delta_y >= 800 and delta_x < 750:
            other_buttons_text_size = delta_y / 28
        if delta_y >= 900 and delta_x < 540:
            other_buttons_text_size = delta_y / 31

    for num_button in num_buttons:
        num_button.config(font=("Arial", int(num_buttons_text_size), "bold"))

    for op_button in operation_buttons:
        op_button.config(font=("Arial", int(other_buttons_text_size), "bold"))

    minis_button.config(font=("Arial", int(other_buttons_text_size), "bold"))
    equals_button.config(font=("Arial", int(other_buttons_text_size), "bold"))
    backspace_button.config(font=("Arial", int(other_buttons_text_size * 0.8), "bold"))
    clear_button.config(font=("Arial", int(other_buttons_text_size), "bold"))

    if delta_x < 1:
        delta_x = 1
    if delta_y < 1:
        delta_y = 1
    master.geometry("%sx%s" % (delta_x, delta_y))

    if delta_x < min_window_width:
        delta_x = min_window_width
    input_field.config(
        font=("Arial", int(other_buttons_text_size / default_button_text_size * default_input_font_size)),
        wraplength=delta_x * default_wraplength / min_window_width)
    output_field.config(
        font=("Arial", int(other_buttons_text_size / default_button_text_size * default_output_font_size)),
        wraplength=delta_x * default_wraplength / min_window_width)


##
# Function that catches releasing the sizegrip button
def sizegrip_button_release(event):
    sizegrip["cursor"] = "arrow"


##
# Function that finds any operation sign in the string
#
# @param str_line Input string
# @return Boolean value
def find_operation_sign(str_line):
    for op in operations_signs:
        op_index = str_line.rfind(op)
        # If the operation sign is in the string and it isn't a part of an exponent
        if op_index != -1 and str_line[op_index - 1:op_index] != "e":
            return True
    return False


##
# Function that checks buttons availability for correct keyboard input
#
# @param value Button input value
# @return Boolean value
def check_num_availability(value):
    if value == "+" and plus_button["state"] == DISABLED:
        return False
    if value == "-" and minis_button["state"] == DISABLED:
        return False
    if value == "*" and multiply_button["state"] == DISABLED:
        return False
    if value == "/" and divide_button["state"] == DISABLED:
        return False
    if value == "√" and root_button["state"] == DISABLED:
        return False
    if value == "!" and factorial_button["state"] == DISABLED:
        return False
    if value == "^" and power_button["state"] == DISABLED:
        return False
    if value == "㏒" and log_button["state"] == DISABLED:
        return False
    if value == "㏑" and nat_log_button["state"] == DISABLED:
        return False
    if value == "," and dec_point_button["state"] == DISABLED:
        return False

    return True


##
# Function that disables all operation buttons (except the minus operation)
def disable_operation_buttons():
    for op_button in operation_buttons:
        op_button.config(state=DISABLED)


##
# Function that enables all operation buttons (except the minus operation)
def enable_operation_buttons():
    for op_button in operation_buttons:
        op_button.config(state=NORMAL)


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
# @return Result ot the function execution
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
            result = f"Zero Division Error:\n" \
                     f"{args[0]} / {args[1]} is NOT possible!"
            state = 1
    elif operator == "!":
        try:
            result = fac(args[0])
            if args[0] > 13:
                result = "{:e}".format(result)
        except ValueError:
            result = f"Factorial Error:" \
                     f"{args[0]} must NOT be decimal or negative!"
            state = 1
    elif operator == "^":
        try:
            result = power(args[0], args[1])
        except ValueError:
            result = f"Power Error: " \
                     f"{args[1]} MUST be a natural number!"
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
            result = f"Natural Logarithm Error: " \
                     f"{args[0]} MUST be greater than zero."
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
# Function that prepares the output string for the output field
#
# @param operator Expression operation
# @param args Expression arguments
# @param result Expression result
# @return String of the equation
def get_output_str(operator, args, result):
    output_str = ""

    # Check numbers negativity (for setting parentheses)
    if args[0] < 0:
        args[0] = f"({args[0]})"
    if float(result) < 0:
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
# Function that finds the result of the last expression
#
# @return Result of the last expression or an empty string
def get_last_result():
    output_str = output_field["text"]  # get the text from output
    i = output_str.rfind("=")  # get the index of '=' sign
    if i == -1:  # if there isn't
        return ""  # return nothing
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
        # While there are parentheses, remove them
        while str_line.find(p, i) != -1:
            i = str_line.find(p, i)
            str_line = str_line[:i] + str_line[i + 1:]
            i += 1
    return str_line


##
# Function that prints the result to the output field
def evaluate(event=None):
    input_str = commas_to_dots(input_field["text"])

    # Feature "Get last result" (not working with basic logarithm properly)
    # If after last expression user will write an equation sign again
    # Last result will copy to the input field
    if input_str == "":
        input_field.config(text=get_last_result())
        if input_field["text"] != "":
            nat_log_button.config(state=DISABLED)
        return

    # Default values
    operator = "?"
    args = []

    # Find the operation sign and set the arguments
    for i in range(len(input_str) - 1, 0, -1):
        if input_str[i] in ["+", "−", "/", "*", "√", "^", "㏒"]:
            operator = input_str[i]
            # if radical index wasn't set
            if operator == "√" and not input_str[:1].isdigit():
                input_str = "2" + input_str
            args.append(float(input_str[:i]))
            args.append(float(input_str[i + 1:]))
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

    exec_output, result = calculate(operator, args)  # get result
    if exec_output == 0:  # if function ends successfully
        output_str = get_output_str(operator, args, result)
        input_field.config(text="")
    else:
        output_str = result  # else put error message to the result string

    output_str = remove_empty_decimal_part(output_str)  # Remove useless decimal parts
    output_str = dots_to_commas(output_str)  # Replace dots with commas
    output_field.config(text=output_str)  # put the result to the output field

    enable_operation_buttons()
    minis_button.config(state=NORMAL)
    dec_point_button.config(state=NORMAL)


# Definition of buttons and binding keys

# NUM Buttons
default_button_text_size = 20

num7_button = Button(master, text="7", command=lambda: input_button_press(7))
num7_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num7_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.36)

master.bind("<Key-7>", lambda value: input_button_press(7))
master.bind("<KP_7>", lambda value: input_button_press(7))

num8_button = Button(master, text="8", command=lambda: input_button_press(8))
num8_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num8_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.36)

master.bind("<Key-8>", lambda value: input_button_press(8))
master.bind("<KP_8>", lambda value: input_button_press(8))

num9_button = Button(master, text="9", command=lambda: input_button_press(9))
num9_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num9_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.36)

master.bind("<Key-9>", lambda value: input_button_press(9))
master.bind("<KP_9>", lambda value: input_button_press(9))

num4_button = Button(master, text="4", command=lambda: input_button_press(4))
num4_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num4_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.51)

master.bind("<Key-4>", lambda value: input_button_press(4))
master.bind("<KP_4>", lambda value: input_button_press(4))

num5_button = Button(master, text="5", command=lambda: input_button_press(5))
num5_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num5_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.51)

master.bind("<Key-5>", lambda value: input_button_press(5))
master.bind("<KP_5>", lambda value: input_button_press(5))

num6_button = Button(master, text="6", command=lambda: input_button_press(6))
num6_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num6_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.51)

master.bind("<Key-6>", lambda value: input_button_press(6))
master.bind("<KP_6>", lambda value: input_button_press(6))

num1_button = Button(master, text="1", command=lambda: input_button_press(1))
num1_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num1_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.66)

master.bind("<Key-1>", lambda value: input_button_press(1))
master.bind("<KP_1>", lambda value: input_button_press(1))

num2_button = Button(master, text="2", command=lambda: input_button_press(2))
num2_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num2_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.66)

master.bind("<Key-2>", lambda value: input_button_press(2))
master.bind("<KP_2>", lambda value: input_button_press(2))

num3_button = Button(master, text="3", command=lambda: input_button_press(3))
num3_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num3_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.66)

master.bind("<Key-3>", lambda value: input_button_press(3))
master.bind("<KP_3>", lambda value: input_button_press(3))

num0_button = Button(master, text="0", command=lambda: input_button_press(0))
num0_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
num0_button.place(relheight=0.15, relwidth=0.5, relx=0, rely=0.81)

master.bind("<Key-0>", lambda value: input_button_press(0))
master.bind("<KP_0>", lambda value: input_button_press(0))

dec_point_button = Button(master, text=",", command=lambda: input_button_press(","))
dec_point_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                        activebackground="#195e89",
                        fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
dec_point_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.81)

master.bind("<Key-comma>", lambda value: input_button_press(","))
master.bind("<KP_Decimal>", lambda value: input_button_press(","))

# Basic operation buttons
divide_button = Button(master, text="÷", command=lambda: input_button_press("/"))
divide_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                     activebackground="#195e89",
                     fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
divide_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.36)

master.bind("<Key-slash>", lambda value: input_button_press("/"))
master.bind("<KP_Divide>", lambda value: input_button_press("/"))

multiply_button = Button(master, text="×", command=lambda: input_button_press("*"))
multiply_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                       activebackground="#195e89",
                       fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
multiply_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.51)

master.bind("<Key-asterisk>", lambda value: input_button_press("*"))
master.bind("<KP_Multiply>", lambda value: input_button_press("*"))

minis_button = Button(master, text="−", command=lambda: input_button_press("-"))
minis_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                    activebackground="#195e89",
                    fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
minis_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.66)

master.bind("<Key-minus>", lambda value: input_button_press("-"))
master.bind("<KP_Subtract>", lambda value: input_button_press("-"))

plus_button = Button(master, text="+", command=lambda: input_button_press("+"))
plus_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
plus_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.81)

master.bind("<Key-plus>", lambda value: input_button_press("+"))
master.bind("<KP_Add>", lambda value: input_button_press("+"))

# Advanced operation buttons
nat_log_button = Button(master, text="㏑", command=lambda: input_button_press("㏑"))
nat_log_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                      activebackground="#195e89",
                      fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
nat_log_button.place(relheight=0.18, relwidth=0.125, relx=0.75, rely=0.18)

master.bind("<Key-n>", lambda value: input_button_press("㏑"))
master.bind("<Key-N>", lambda value: input_button_press("㏑"))

log_button = Button(master, text="㏒", command=lambda: input_button_press("㏒"))
log_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                  activebackground="#195e89",
                  fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
log_button.place(relheight=0.18, relwidth=0.125, relx=0.875, rely=0.18)

master.bind("<Key-l>", lambda value: input_button_press("㏒"))
master.bind("<Key-L>", lambda value: input_button_press("㏒"))

factorial_button = Button(master, text="n!", command=lambda: input_button_press("!"))
factorial_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                        activebackground="#195e89",
                        fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
factorial_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.36)

master.bind("<Key-exclam>", lambda value: input_button_press("!"))

root_button = Button(master, text="√", command=lambda: input_button_press("√"))
root_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                   activebackground="#195e89",
                   fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
root_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.51)

master.bind("<Key-r>", lambda value: input_button_press("√"))
master.bind("<Key-R>", lambda value: input_button_press("√"))

power_button = Button(master, text="xⁿ", command=lambda: input_button_press("^"))
power_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                    activebackground="#195e89",
                    fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
power_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.66)

master.bind("<Key-asciicircum>", lambda value: input_button_press("^"))

# Equals button
equals_button = Button(master, text="=", command=evaluate)
equals_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                     activebackground="#195e89",
                     fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
equals_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.81)

master.bind("<Return>", evaluate)
master.bind("<KP_Enter>", evaluate)
master.bind("<Key-equal>", evaluate)

# Special buttons
backspace_button = Button(master, text="⌫", command=backspace_button_click)
backspace_button.config(relief=FLAT, font=("Arial", int(0.9 * default_button_text_size), "bold"), bg="#003d63",
                        activebackground="#195e89",
                        fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
backspace_button.place(relheight=0.18, relwidth=0.125, relx=0.75, rely=0)

master.bind("<Key-BackSpace>", backspace_button_click)
master.bind("<Key-Delete>", backspace_button_click)

clear_button = Button(master, text="C", command=clear_button_click)
clear_button.config(relief=FLAT, font=("Arial", default_button_text_size, "bold"), bg="#003d63",
                    activebackground="#195e89",
                    fg="#ffffff", activeforeground="#ffffff", highlightbackground="black")
clear_button.place(relheight=0.18, relwidth=0.125, relx=0.875, rely=0)

master.bind("<Key-c>", clear_button_click)
master.bind("<Key-C>", clear_button_click)

master.bind("<Escape>", lambda value: master.destroy())

# Sizegrip binds
sizegrip.bind("<ButtonPress-1>", sizegrip_button_press)
sizegrip.bind("<B1-Motion>", resize_main_window)
sizegrip.bind("<ButtonRelease-1>", sizegrip_button_release)

num_buttons = [num0_button, num1_button, num2_button, num3_button, num4_button, num5_button, num6_button,
               num7_button, num8_button, num9_button]

operation_buttons = [plus_button, multiply_button, divide_button, power_button, root_button,
                     factorial_button, log_button, nat_log_button, dec_point_button]

# MAIN loop
master.mainloop()
