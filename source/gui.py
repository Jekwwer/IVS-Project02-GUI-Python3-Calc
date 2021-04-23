# GUI

##
# @file     gui.py
# @brief    Graphic User Interface for the mathematical library
# @authors  Evgenii Shiliaev  (xshili00)
# @authors  Marko Kubrachenko (xkubra00)
# @authors  Pavel Beneš       (xbenes58)

from tkinter import *
from tkinter import ttk
from math_lib import *

# Windows parameters
min_main_window_width = 350
min_main_window_height = 370
min_additional_window_width = 400
min_additional_window_height = 404
# Text parameters
wraplength_difference = 25
default_button_text_size = 20
default_font = "Arial"
# Custom colors
dark_red = ["#630000", "#891919"]
dark_orange = ["#633700", "#894f19"]
dark_yellow = ["#616300", "#897c19"]
dark_green = ["#006301", "#19891a"]
dark_cyan = ["#006361", "#198689"]
dark_blue = ["#003d63", "#195e89"]
dark_violet = ["#490063", "#6e1989"]
default_color = dark_blue
default_foregroung_color = "#ffffff"

# Custom widgets


##
# Class of the main window I/O fields
class MainWindowField(Label):
    ##
    # Constructor of the main window I/O fields
    #
    # @param font_size font_size
    # @param wraplength Label wraplength
    def __init__(self, font_size, wraplength):
        super().__init__()
        self["borderwidth"] = 1
        self["bg"] = "#dadada"
        self["relief"] = "solid"
        self["font"] = f"{default_font} {font_size}"
        self["wraplength"] = wraplength


##
# Class of the main window menu
class MainWindowButton(Button):
    ##
    # Constructor of the main window button
    #
    # @param parent Parent window
    # @param text On-button text
    # @param command Button-click command
    def __init__(self, parent, text, command):
        Button.__init__(self, parent)
        self["relief"] = FLAT
        self["fg"] = default_foregroung_color
        self["highlightbackground"] = "black"
        self["text"] = text
        self["font"] = f"{default_font} {default_button_text_size} bold"
        self["command"] = command

        self.set_color(default_color)

    ##
    # Function that sets the button text size by ratio of the default size
    #
    # @param font_size_ratio Ratio of the final font size
    def set_font_size_by_ratio(self, font_size_ratio):
        self["font"] = f"{default_font} {int(font_size_ratio * default_button_text_size)} bold"

    ##
    # Function that sets the button color
    #
    # @param color list of background and active background colors
    def set_color(self, color):
        self["bg"] = color[0]
        self["activebackground"] = color[1]


##
# Class of the main window menu
class CustomMenu(Menu):
    ##
    # Constructor of the main window menu
    #
    # @param parent Parent window
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self["fg"] = default_foregroung_color
        self["activeforeground"] = default_foregroung_color
        self["tearoff"] = 0
        self.set_color(default_color)

    ##
    # Function that sets the menu color
    #
    # @param color List of background and active background colors
    def set_color(self, color):
        self["bg"] = color[0]
        self["activebackground"] = color[1]

    ##
    # Function that a new command to the menu
    #
    # @param label Command label
    # @param color List of background and active background colors
    # @param command Executing command
    def add_new_command(self, label, color, command):
        if color is None:
            self.add_command(label=label, command=command, font=default_font)
        else:
            self.add_command(label=label, activebackground=color[1], command=command, font=default_font)


##
# Class of the scrollbar
class Scrollbar(Frame):
    ##
    # Constructor of the window scrollbar
    #
    # @param parent Parent window
    def __init__(self, parent):
        Frame.__init__(self, parent)

        scroll_frame = Frame(parent)
        scroll_frame.pack(fill=BOTH, expand=1)

        scroll_canvas = Canvas(scroll_frame)
        scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = ttk.Scrollbar(scroll_frame, orient=VERTICAL, command=scroll_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        scroll_canvas.configure(yscrollcommand=scrollbar.set)
        scroll_canvas.bind("<Configure>", lambda event: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))

        self.scroll_content_frame = Frame(scroll_canvas)
        scroll_canvas.create_window((0, 0), window=self.scroll_content_frame, anchor="nw")

    ##
    # Function that returns the scroll content frame
    # @brief  This function makes possible to correctly add new scrollable widgets to the scrollbar frame
    #
    # @return Frame that contains all scrollbar's widgets
    def return_content_frame(self):
        return self.scroll_content_frame


##
# Class of the sizegrip
class Sizegrip(Frame):
    ##
    # Constructor of the window sizegrip
    #
    # @param parent Parent window
    def __init__(self, parent):
        Frame.__init__(self, parent)

        sizegrip_frame = Frame(self, bg="#dadada", highlightbackground="black")
        sizegrip_frame.pack(side="bottom", fill=X)

        ttk.Style().layout("Sizer.TLabel", [("Sizegrip.sizegrip", {"sticky": "se", "side": "bottom"})])
        sizegrip = ttk.Label(sizegrip_frame, style="Sizer.TLabel")
        sizegrip.pack(anchor="se")

        # Sizegrip binds
        sizegrip.bind("<ButtonPress-1>", lambda event: sizegrip_button_press(event, sizegrip))
        if parent == master:
            sizegrip.bind("<B1-Motion>", lambda event: resize_main_window(event))
        else:
            parent_labels, font_size = parent.get_params()
            sizegrip.bind("<B1-Motion>",
                          lambda event: resize_additional_window(event, parent, parent_labels, font_size))

        sizegrip.bind("<ButtonRelease-1>", lambda event: sizegrip_button_release(event, sizegrip))


# Additional windows

##
# Class of the About window
class AboutWindow(Toplevel):
    ##
    # Constructor of the About window
    def __init__(self):
        super().__init__()
        self.title("About")

        # Put on the Left upper center part of the screen
        add_x_position = int(master.winfo_screenwidth() / 2 + min_additional_window_width / 2)
        add_y_position = y_position
        self.geometry(f"{min_additional_window_width}x{min_additional_window_height}+{add_x_position}+{add_y_position}")
        self.minsize(min_additional_window_width, min_additional_window_height)
        self.resizable(False, False)

        min_label_width = min_additional_window_width - wraplength_difference

        scrollbar = Scrollbar(self)
        scrollbar_frame = scrollbar.return_content_frame()
        scrollbar.pack()

        # Put some labels
        self.default_font_size = 13
        self.labels_list = []
        app_about_label = Label(scrollbar_frame, text="This calculator application was created as the 2nd project "
                                                      "of the \"Practical Aspects of Software Design\" subject "
                                                      "by the team \"Blue Hair is the Way\n",
                                font=(default_font, self.default_font_size),
                                wraplength=min_label_width,
                                justify="left")
        app_about_label.pack()
        self.labels_list.append(app_about_label)

        authors_label = Label(scrollbar_frame, text="Authors:\n"
                                                    "• xshili00 Evgenii Shiliaev\n"
                                                    "• xbenes58 Pavel Beneš\n"
                                                    "• xkubra00 Marko Kubrachenko\n"
                                                    "• xbrazd22 Šimon Brázda", font=("Courier", self.default_font_size),
                              wraplength=min_label_width,
                              justify="left")
        authors_label.pack()
        self.labels_list.append(authors_label)

        Sizegrip(self).pack(anchor="se")

        # Exit About window shortcut
        self.bind("<Escape>", lambda event: self.destroy())

    ##
    # Function that returns the labels list with their default font size
    # @brief  This function makes possible to change the window labels size via the sizegrip
    #
    # @return List of the window labels
    # @return Default labels' font size
    def get_params(self):
        return self.labels_list, self.default_font_size


##
# Class of the Help window
class HelpWindow(Toplevel):
    ##
    # Constructor of the Help window
    def __init__(self):
        super().__init__()
        self.title("Help")

        # Put on the Left upper center part of the screen
        add_x_position = int(master.winfo_screenwidth() / 2 - 1.5 * min_additional_window_width)
        add_y_position = y_position
        self.geometry(f"{min_additional_window_width}x{min_additional_window_height}+{add_x_position}+{add_y_position}")
        self.minsize(min_additional_window_width, min_additional_window_height)
        self.resizable(False, False)

        # Help window scrollbar
        scrollbar = Scrollbar(self)
        scrollbar_frame = scrollbar.return_content_frame()
        scrollbar.pack()

        # Put some labels
        self.labels_list = []
        self.default_font_size = 13
        help_label = Label(scrollbar_frame, text="This is a help window", font=(default_font, self.default_font_size))
        help_label.pack()

        self.labels_list.append(help_label)

        Sizegrip(self).pack(anchor="se")

        # Exit About window shortcut
        self.bind("<Escape>", lambda event: self.destroy())

    ##
    # Function that returns the labels list with their default font size
    # @brief  This function makes possible to change the window labels size via the sizegrip
    #
    # @return List of the window labels
    # @return Default labels' font size
    def get_params(self):
        return self.labels_list, self.default_font_size
    # TODO get rid of code duplications


##
# Function that opens the Help window
def open_help_window():
    global help_window
    # If the window is opened, focus on it
    try:
        if help_window.state() == "normal":
            help_window.focus()
    # Else open it
    except (NameError, TclError):
        help_window = HelpWindow()


##
# Function that opens the About window
def open_about_window():
    global about_window
    # If the window is opened, focus on it
    try:
        if about_window.state() == "normal":
            about_window.focus()
    # Else open it
    except (NameError, TclError):
        about_window = AboutWindow()


# Operation list
operations_signs = ["+", "−", "/", "*", "!", "^", "√", "㏒", "㏑"]


# Functions

##
# Function of adding button value to the input field
#
# @todo disable numbers after factorial sign
#
# @param value Button value
def input_button_press(value):
    # If button is disabled (for keyboard input)
    if not check_button_availability(value):
        return

    # Get string from the input
    input_str = input_field["text"]

    if input_str[-1:] == value == '-':
        return

    if input_str == "" and (str(value).isdigit()):
        enable_operation_buttons()

    if len(input_str) == 1 and (str(value).isdigit()):
        enable_operation_buttons()

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
        is_operator, op_index = find_operation_sign(input_str)
        if "," in input_str[op_index:]:
            dec_point_button.config(state=DISABLED)
        else:
            dec_point_button.config(state=NORMAL)

    # Feature "Change the operation sign"
    # Before setting 2nd operand in such operations
    # user can change the operation sign by setting the other one
    # without a Backspace or Clear button call
    if input_str[-1:] in operations_signs and value in operations_signs:
        is_operator, op_index = find_operation_sign(input_str)
        if is_operator and input_str[:op_index] != "":
            input_str = input_str[:-1]
        else:
            return

    if (input_str[-1:].isdigit() or input_str[-1:] == ",") and value == "-":
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
def clear_button_click():
    if input_field["text"] == "":
        output_field["text"] = ""
        disable_operation_buttons()
        root_button.config(state=NORMAL)
        dec_point_button.config(state=NORMAL)
        minis_button.config(state=NORMAL)
        return

    input_field.config(text="")
    if output_field["text"] == "":
        disable_operation_buttons()
        root_button.config(state=NORMAL)
        dec_point_button.config(state=NORMAL)
        minis_button.config(state=NORMAL)
        return

    # Enable disabled buttons
    dec_point_button.config(state=NORMAL)
    minis_button.config(state=NORMAL)
    enable_operation_buttons()


##
# Function that deletes the last character from the input field
def backspace_button_click():
    input_str = str(input_field["text"])
    # If input field is empty
    if input_str[:-1] == "" or len(input_str) == 1:
        clear_button_click()
        return
    input_field.config(text=input_str[:-1])
    if input_str[:-1] == "-":
        disable_operation_buttons()
        root_button.config(state=NORMAL)
        dec_point_button.config(state=NORMAL)
        minis_button.config(state=NORMAL)
    # If last character was a decimal point, enable the decimal point button
    if input_str[-1:] == ",":
        dec_point_button.config(state=NORMAL)
    # If last character was an operation sign, enable the operation buttons
    if input_str[-2:-1] in operations_signs or input_str[-1:] in operations_signs:
        enable_operation_buttons()
        minis_button.config(state=NORMAL)


##
# Function that catches pressing the sizegrip button
def sizegrip_button_press(event, sizegrip):
    sizegrip["cursor"] = "bottom_right_corner"


##
# Function that resizes the additional app windows
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
        if delta_x >= min_additional_window_width:
            label_font_size = int(delta_x / min_additional_window_width * default_font_size)
        labels[i].config(font=(label_font_config[0], label_font_size))
        if delta_x < min_additional_window_width:
            delta_x = min_additional_window_width
        labels[i].config(wraplength=delta_x - wraplength_difference)


##
# Function that resizes the main app window
#
# @todo Refactoring
def resize_main_window(event):
    delta_x = event.x_root - master.winfo_rootx()
    delta_y = event.y_root - master.winfo_rooty()

    num_buttons_text_size = other_buttons_text_size = default_button_text_size

    if delta_x / 16 > delta_y / 9:
        if delta_x >= min_main_window_width:
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
        if delta_y >= min_main_window_height:
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
        num_button.config(font=(default_font, int(num_buttons_text_size), "bold"))

    for op_button in operation_buttons:
        op_button.config(font=(default_font, int(other_buttons_text_size), "bold"))

    minis_button.config(font=(default_font, int(other_buttons_text_size), "bold"))
    equals_button.config(font=(default_font, int(other_buttons_text_size), "bold"))
    backspace_button.config(font=(default_font, int(other_buttons_text_size * 0.8), "bold"))
    clear_button.config(font=(default_font, int(other_buttons_text_size), "bold"))

    if delta_x < 1:
        delta_x = 1
    if delta_y < 1:
        delta_y = 1
    master.geometry("%sx%s" % (delta_x, delta_y))

    if delta_x < min_main_window_width:
        delta_x = min_main_window_width
    input_field.config(
        font=(default_font, int(other_buttons_text_size / default_button_text_size * default_input_font_size)),
        wraplength=delta_x * default_wraplength / min_main_window_width)
    output_field.config(
        font=(default_font, int(other_buttons_text_size / default_button_text_size * default_output_font_size)),
        wraplength=delta_x * default_wraplength / min_main_window_width)


##
# Function that catches releasing the sizegrip button
def sizegrip_button_release(event, sizegrip):
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
            return True, op_index
    return False


##
# Function that checks buttons availability for correct keyboard input
#
# @param value Button input value
# @return Boolean value
def check_button_availability(value):
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

    if input_field["text"] == "":
        root_button.config(state=NORMAL)
        nat_log_button.config(state=NORMAL)
        dec_point_button.config(state=NORMAL)


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
# @todo Factorial bound
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
        return remove_parentheses(output_str[i + 2:])


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
def evaluate():
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
    for i in range(len(input_str) - 1, -1, -1):
        if input_str[i] in ["+", "−", "/", "*", "√", "^", "㏒"]:
            operator = input_str[i]
            # if radical index wasn't set
            if operator == "√" and not input_str[:1].isdigit():
                input_str = "2" + input_str
                i += 1
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


##
# Function that changes the application color theme
#
# @param color list of background and active background colors
def change_theme(color):
    for button in all_buttons:
        button.set_color(color)
    for menu in menu_list:
        menu.set_color(color)


if __name__ == "__main__":
    # Main window parameters
    master = Tk()
    master.title("WaterLift Calculator")
    master.resizable(False, False)

    # Upper center screen coordinates
    x_position = int(master.winfo_screenwidth() / 2 - min_main_window_width / 2)
    y_position = int(master.winfo_screenheight() / 3 - min_main_window_height / 2)

    # Put thw  main window to the (x,y)
    master.geometry(f"{min_main_window_width}x{min_main_window_height}+{x_position}+{y_position}")
    master.minsize(min_main_window_width, min_main_window_height)

    # Main window menu
    main_menu = CustomMenu(master)
    main_menu.add_new_command(label="Help", color=None, command=open_help_window)

    # Settings menu
    settings_menu = CustomMenu(master)
    set_color_menu = CustomMenu(master)

    set_color_menu.add_new_command("Dark Red", dark_red, lambda: change_theme(dark_red))
    set_color_menu.add_new_command("Dark Orange", dark_orange, lambda: change_theme(dark_orange))
    set_color_menu.add_new_command("Dark Yellow", dark_yellow, lambda: change_theme(dark_yellow))
    set_color_menu.add_new_command("Dark Green", dark_green, lambda: change_theme(dark_green))
    set_color_menu.add_new_command("Dark Cyan", dark_cyan, lambda: change_theme(dark_cyan))
    set_color_menu.add_new_command("Dark Blue", dark_blue, lambda: change_theme(dark_blue))
    set_color_menu.add_new_command("Dark Violet", dark_violet, lambda: change_theme(dark_violet))
    settings_menu.add_cascade(label="Set color theme", font=default_font, menu=set_color_menu)
    main_menu.add_cascade(label="Settings", font=default_font, menu=settings_menu)

    main_menu.add_new_command(label="About", color=None, command=open_about_window)

    master.config(menu=main_menu)

    menu_list = [main_menu, settings_menu, set_color_menu]

    # I/O Fields
    field_width_ratio = 0.75
    default_wraplength = int(field_width_ratio * min_main_window_width - wraplength_difference)
    default_input_font_size = 18
    input_field = MainWindowField(default_input_font_size, default_wraplength)
    input_field.place(relheight=0.18, relwidth=field_width_ratio, relx=0, rely=0)

    default_output_font_size = 14
    output_field = MainWindowField(default_output_font_size, default_wraplength)
    output_field.place(relheight=0.18, relwidth=field_width_ratio, relx=0, rely=0.18)

    # Definition of buttons and binding keys
    # NUM Buttons
    num7_button = MainWindowButton(master, "7", lambda: input_button_press(7))
    num7_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.36)
    master.bind("<Key-7>", lambda value: input_button_press(7))
    master.bind("<KP_7>", lambda value: input_button_press(7))

    num8_button = MainWindowButton(master, "8", lambda: input_button_press(8))
    num8_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.36)
    master.bind("<Key-8>", lambda value: input_button_press(8))
    master.bind("<KP_8>", lambda value: input_button_press(8))

    num9_button = MainWindowButton(master, "9", lambda: input_button_press(9))
    num9_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.36)
    master.bind("<Key-9>", lambda value: input_button_press(9))
    master.bind("<KP_9>", lambda value: input_button_press(9))

    num4_button = MainWindowButton(master, "4", lambda: input_button_press(4))
    num4_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.51)
    master.bind("<Key-4>", lambda value: input_button_press(4))
    master.bind("<KP_4>", lambda value: input_button_press(4))

    num5_button = MainWindowButton(master, "5", lambda: input_button_press(5))
    num5_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.51)
    master.bind("<Key-5>", lambda value: input_button_press(5))
    master.bind("<KP_5>", lambda value: input_button_press(5))

    num6_button = MainWindowButton(master, "6", lambda: input_button_press(6))
    num6_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.51)
    master.bind("<Key-6>", lambda value: input_button_press(6))
    master.bind("<KP_6>", lambda value: input_button_press(6))

    num1_button = MainWindowButton(master, "1", lambda: input_button_press(1))
    num1_button.place(relheight=0.15, relwidth=0.25, relx=0, rely=0.66)
    master.bind("<Key-1>", lambda value: input_button_press(1))
    master.bind("<KP_1>", lambda value: input_button_press(1))

    num2_button = MainWindowButton(master, "2", lambda: input_button_press(2))
    num2_button.place(relheight=0.15, relwidth=0.25, relx=0.25, rely=0.66)
    master.bind("<Key-2>", lambda value: input_button_press(2))
    master.bind("<KP_2>", lambda value: input_button_press(2))

    num3_button = MainWindowButton(master, "3", lambda: input_button_press(3))
    num3_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.66)
    master.bind("<Key-3>", lambda value: input_button_press(3))
    master.bind("<KP_3>", lambda value: input_button_press(3))

    num0_button = MainWindowButton(master, "0", lambda: input_button_press(0))
    num0_button.place(relheight=0.15, relwidth=0.5, relx=0, rely=0.81)
    master.bind("<Key-0>", lambda value: input_button_press(0))
    master.bind("<KP_0>", lambda value: input_button_press(0))

    dec_point_button = MainWindowButton(master, ",", lambda: input_button_press(","))
    dec_point_button.place(relheight=0.15, relwidth=0.25, relx=0.5, rely=0.81)
    master.bind("<Key-comma>", lambda value: input_button_press(","))
    master.bind("<KP_Decimal>", lambda value: input_button_press(","))

    # Basic operation buttons
    divide_button = MainWindowButton(master, "÷", lambda: input_button_press("/"))
    divide_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.36)
    master.bind("<Key-slash>", lambda value: input_button_press("/"))
    master.bind("<KP_Divide>", lambda value: input_button_press("/"))

    multiply_button = MainWindowButton(master, "×", lambda: input_button_press("*"))
    multiply_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.51)
    master.bind("<Key-asterisk>", lambda value: input_button_press("*"))
    master.bind("<KP_Multiply>", lambda value: input_button_press("*"))

    minis_button = MainWindowButton(master, "−", lambda: input_button_press("-"))
    minis_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.66)
    master.bind("<Key-minus>", lambda value: input_button_press("-"))
    master.bind("<KP_Subtract>", lambda value: input_button_press("-"))

    plus_button = MainWindowButton(master, "+", lambda: input_button_press("+"))
    plus_button.place(relheight=0.15, relwidth=0.125, relx=0.75, rely=0.81)
    master.bind("<Key-plus>", lambda value: input_button_press("+"))
    master.bind("<KP_Add>", lambda value: input_button_press("+"))

    # Advanced operation buttons
    nat_log_button = MainWindowButton(master, "㏑", lambda: input_button_press("㏑"))
    nat_log_button.place(relheight=0.18, relwidth=0.125, relx=0.75, rely=0.18)
    master.bind("<Key-n>", lambda value: input_button_press("㏑"))
    master.bind("<Key-N>", lambda value: input_button_press("㏑"))

    log_button = MainWindowButton(master, "㏒", lambda: input_button_press("㏒"))
    log_button.place(relheight=0.18, relwidth=0.125, relx=0.875, rely=0.18)
    master.bind("<Key-l>", lambda value: input_button_press("㏒"))
    master.bind("<Key-L>", lambda value: input_button_press("㏒"))

    factorial_button = MainWindowButton(master, "n!", lambda: input_button_press("!"))
    factorial_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.36)
    master.bind("<Key-exclam>", lambda value: input_button_press("!"))

    root_button = MainWindowButton(master, "√", lambda: input_button_press("√"))
    root_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.51)
    master.bind("<Key-r>", lambda value: input_button_press("√"))
    master.bind("<Key-R>", lambda value: input_button_press("√"))

    power_button = MainWindowButton(master, "xⁿ", lambda: input_button_press("^"))
    power_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.66)
    master.bind("<Key-asciicircum>", lambda value: input_button_press("^"))

    # Equals button
    equals_button = MainWindowButton(master, "=", command=evaluate)
    equals_button.place(relheight=0.15, relwidth=0.125, relx=0.875, rely=0.81)
    master.bind("<Return>", evaluate)
    master.bind("<KP_Enter>", evaluate)
    master.bind("<Key-equal>", evaluate)

    # Special buttons
    backspace_button = MainWindowButton(master, "⌫", backspace_button_click)
    backspace_button.place(relheight=0.18, relwidth=0.125, relx=0.75, rely=0)
    backspace_button.set_font_size_by_ratio(0.9)
    master.bind("<Key-BackSpace>", backspace_button_click)
    master.bind("<Key-Delete>", backspace_button_click)

    clear_button = MainWindowButton(master, "C", clear_button_click)
    clear_button.place(relheight=0.18, relwidth=0.125, relx=0.875, rely=0)
    master.bind("<Key-c>", clear_button_click)
    master.bind("<Key-C>", clear_button_click)

    # Close the application by key
    master.bind("<Escape>", lambda event: master.destroy())

    # Help hotkeys
    master.bind("<H>", lambda event: open_help_window())
    master.bind("<h>", lambda event: open_help_window())

    # Object lists (for easy parameters changing)
    num_buttons = [num0_button, num1_button, num2_button, num3_button, num4_button, num5_button, num6_button,
                   num7_button, num8_button, num9_button]

    operation_buttons = [plus_button, multiply_button, divide_button, power_button, root_button,
                         factorial_button, log_button, nat_log_button, dec_point_button]

    special_buttons = [backspace_button, clear_button, equals_button]

    all_buttons = num_buttons + operation_buttons + special_buttons + [minis_button]

    # Sizegrip
    main_window_sizegrip = Sizegrip(master).pack(anchor="se", side=BOTTOM)

    # Disable operation buttons on the start (before the first input)
    disable_operation_buttons()

    # Application loop
    master.mainloop()
