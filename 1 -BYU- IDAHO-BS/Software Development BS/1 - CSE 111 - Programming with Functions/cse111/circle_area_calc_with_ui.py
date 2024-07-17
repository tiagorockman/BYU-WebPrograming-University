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

    lbl_slow = Label(frm_main, width=3)

    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    input_radius.grid(      row=0, column=1, padx=3, pady=3)
    btn_calculate.grid(row=0, column=2, padx=0, pady=3)

    lbl_slow.grid(      row=1, column=0, padx=3, pady=3)
    
    def calculate_circle_area(radius):
        area = math.pi * (radius ** 2)
        return area

if __name__ == "__main__":
    main()
