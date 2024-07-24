import tkinter as tk
from tkinter import Frame, Label, Button, filedialog
import os


def list_folder_files(folder_path):
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError as err:
        return []
    except ValueError as verr:
        log_error(err, "List files on folder Selected")

def list_folder_selection_files(folder_path):
    try:
        files = list_folder_files(folder_path)       
        entry_text_area.delete(1.0, tk.END) #clrear the existing text
        entry_text_area.insert(tk.END, "The files below will be renamed, as you choose FROM TEXT and TO TEXT inputs above.\nIf you choose FROM='B' TO='A' all B letters will be renamed to A.\n\n", "first_line_alert")
        
        if len(files) == 0:
            entry_text_area.insert(tk.END, "There is no file in the folder selected.", "list_text")
        else:
            entry_text_area.insert(tk.END, "List of files:\n", "list_text")

        for file in files:
            entry_text_area.insert(tk.END, f"{file}\n")
    except ValueError as err:
        log_error(err, "List files on folder Selected")

def create_window():
    # Create the Tk root object.
    root = tk.Tk()
    #window size
    root.geometry('520x420')

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
    
    global folder_label #using global to be viewd for all code 
    folder_label = tk.Label(frm_main, text="", fg="white", bg="black")

    global entry_text_area #using global to be viewd for all code 
    lbl_text_area = tk.Label(frm_main, text="Files Details:", fg='white', bg='black', justify='left')
    entry_text_area= tk.Text(frm_main, fg='black', font=('Arial', 12), wrap='word', height=10, width=55)

    rename_action = tk.Button(frm_main, text="Rename", command=rename, font=('Arial', 12), width=8, background='blue', foreground='white')
    clear_action = tk.Button(frm_main, text="Clear", command=clear, font=('Arial', 12), width=8, background='yellow', foreground='black')

    # # Layout all the labels and buttons in a grid.
    lbl_text_from.grid(row=0, column=0, padx=2, pady=4, sticky="w")
    entry_text_from.grid(row=1, column=0, padx=2, pady=4, sticky="w")

    lbl_text_to.grid(row=0, column=0, padx=302, pady=4, sticky="w")
    entry_text_to.grid(row=1, column=0, padx=302, pady=4, sticky="w")

    lbl_text_folder.grid(row=3, column=0, padx=6, pady=10, sticky="w")
    select_folder_button.grid(row=4, column=0, padx=6, pady=4, sticky="w")
    folder_label.grid(row=4, column=0, padx=120, pady=6, sticky="w")
    
    
    lbl_text_area.grid(row=6, column=0, padx=6, pady=12, sticky="w")
    entry_text_area.grid(row=7, column=0, padx=6, pady=3, sticky="w")
    #Diferent log color line
    entry_text_area.tag_configure("first_line_alert", foreground='orange', font=('Arial', 12, 'italic'))
    entry_text_area.tag_configure("list_text", foreground='black', font=('Arial', 12, 'italic'))

    rename_action.grid(row=8, column=0, padx=1, pady=5, )
    clear_action.grid(row=8, column=0, padx=10, pady=5,sticky='w')
    

def select_folder():
    try:
        folder_path = filedialog.askdirectory()
        if folder_path:
            folder_label.config(text=folder_path)
            list_folder_selection_files(folder_path)
    except ValueError as err:
        log_error(err, "Selec Folder")



def rename():
    try:
        print("ok")
    except ValueError as err:
        log_error(err, "List files on folder Selected")

def clear():
    try:
        print("ok")
    except ValueError as err:
        log_error(err, "List files on folder Selected")

def log_error(err, source):
    entry_text_area.delete(1.0, tk.END)
    entry_text_area.insert(f"Error source: {source} \nError message: {err}")

    
if __name__ == "__main__":
    create_window()
