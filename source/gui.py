from tkinter import *

# the root of the program
root = Tk()

# Fields
input_field = Entry(root)
input_field.insert(0, "Enter your expression")
input_field.grid(row=0, columnspan=3)

output_field = Label(root)
output_field.grid(row=1, columnspan=3)

# NUM Buttons
num7_button = Button(root, text="7")
num7_button.grid(row=2, column=0)
num8_button = Button(root, text="8")
num8_button.grid(row=2, column=1)
num9_button = Button(root, text="9")
num9_button.grid(row=2, column=2)

num4_button = Button(root, text="4")
num4_button.grid(row=3, column=0)
num5_button = Button(root, text="5")
num5_button.grid(row=3, column=1)
num6_button = Button(root, text="6")
num6_button.grid(row=3, column=2)

num1_button = Button(root, text="1")
num1_button.grid(row=4, column=0)
num2_button = Button(root, text="2")
num2_button.grid(row=4, column=1)
num3_button = Button(root, text="3")
num3_button.grid(row=4, column=2)

num0_button = Button(root, text="0")
num0_button.grid(row=5, columnspan=2)
dec_point_button = Button(root, text=",")
dec_point_button.grid(row=5, column=2)

# Operation buttons
divide_button = Button(root, text="\u00F7")
divide_button.grid(row=2, column=4)
multiply_button = Button(root, text="\u00D7")
multiply_button.grid(row=3, column=4)
minis_button = Button(root, text="\u2212")
minis_button.grid(row=4, column=4)
plus_button = Button(root, text="\u002B")
plus_button.grid(row=5, column=4)

# MAIN loop
root.mainloop()
