import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()
    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Heart Rate")
    frm_main.pack(padx=15, pady=15, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()




def populate_main_window(frm_main):
    lbl_radius = Label(frm_main, text="Inform the circle radius:")

    input_radius = IntEntry(frm_main, width=8, lower_bound=12, upper_bound=90)

    btn_calculate = Button(frm_main, text="Calculate")

    lbl_result = Label(frm_main, width=30)

    btn_clear = Button(frm_main, text="Clear")

    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    input_radius.grid(      row=0, column=1, padx=3, pady=3)
    btn_calculate.grid(row=0, column=2, padx=0, pady=3)

    lbl_result.grid(      row=1, column=0, padx=3, pady=3)
    btn_clear.grid(row=3,column=0,padx=3, pady=3)

    def clear_window():
        btn_clear.focus()
        input_radius.clear()
        lbl_result.config(text="")
        input_radius.focus()
    
    def calculate_circle_area():
        try:
            radius = input_radius.get()
            area = math.pi * (radius ** 2)
            lbl_result.config(text=f"The circle area is: {area:.2f}")
        except ValueError as type_error:
            lbl_result.config(text=type_error)
    
    btn_calculate.config(command=calculate_circle_area)
    btn_clear.config(comma=clear_window)
    lbl_result.focus()

if __name__ == "__main__":
    main()
