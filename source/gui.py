from tkinter import *

# the root of the program
root = Tk()

# Fields
input_field = Entry(root)
input_field.insert(0, "Enter your expression")
input_field.grid(row=0, column=0)

output_field = Label(root)
output_field.grid(row=1, column=0)

# MAIN loop
root.mainloop()
