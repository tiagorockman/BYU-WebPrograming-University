import tkinter as tk
from tkinter import Frame, Label, Button, filedialog


def main():
    # Create the Tk root object.
    root = tk.Tk()
    #window size
    root.geometry('520x390')

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("File Renamer")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    populate_main_window(frm_main)
 
    root.mainloop()

def populate_main_window(frm_main):
    # """Populate the form
    lbl_text_from = tk.Label(frm_main, text="FROM TEXT:", fg='white', bg='black', justify='center')
    entry_text_from = tk.Entry(frm_main, fg='black', font=('Arial', 12))

    lbl_text_to = tk.Label(frm_main, text="TO TEXT:", fg='white', bg='black', justify='center')
    entry_text_to= tk.Entry(frm_main, fg='black', font=('Arial', 12))

    lbl_text_folder = tk.Label(frm_main, text="Select a folder where the files is located:", fg='white', bg='black', justify='left')
    select_folder_button = tk.Button(frm_main, text="Choose Folder", command=select_folder)
    global folder_label
    folder_label = tk.Label(frm_main, text="", fg="white", bg="black")

    lbl_text_area = tk.Label(frm_main, text="Files Details:", fg='white', bg='black', justify='left')
    entry_text_area= tk.Text(frm_main, fg='black', font=('Arial', 12), wrap='word', height=10, width=50)

    rename_action = tk.Button(frm_main, text="Rename", command='')

    # # Layout all the labels and buttons in a grid.
    lbl_text_from.grid(row=0, column=0, padx=2, pady=2, sticky="w")
    entry_text_from.grid(row=1, column=0, padx=2, pady=2, sticky="w")

    lbl_text_to.grid(row=0, column=0, padx=302, pady=2, sticky="w")
    entry_text_to.grid(row=1, column=0, padx=302, pady=2, sticky="w")

    lbl_text_folder.grid(row=3, column=0, padx=6, pady=5, sticky="w")
    select_folder_button.grid(row=4, column=0, padx=6, pady=2, sticky="w")
    folder_label.grid(row=4, column=0, padx=120, pady=2, sticky="w")
    
    lbl_text_area.grid(row=6, column=0, padx=6, pady=2, sticky="w")
    entry_text_area.grid(row=7, column=0, padx=6, pady=5, sticky="w")

    rename_action.grid(row=8, column=0, padx=6, pady=5, sticky="n")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)

    
if __name__ == "__main__":
    main()
