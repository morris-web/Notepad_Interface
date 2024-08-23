from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import Scrollbar


def save_file():
    try:
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                             filetypes=[('Text files', '*.txt')])
        if open_file is None:
            return
        text = entry.get(1.0, END)
        open_file.write(text)
        open_file.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def open_file():
    try:
        file = filedialog.askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
        if file is not None:
            content = file.read()
            entry.delete(1.0, END)
            entry.insert(END, content)
            file.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file: {e}")

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False, False)

# Create and place buttons
b1 = Button(root, width=20, height=2, bg='#fff', text='Save File', command=save_file)
b1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
b2 = Button(root, width=20, height=2, bg='#fff', text='Open File', command=open_file)
b2.grid(row=0, column=1, padx=10, pady=10, sticky=E)

# Create and place text widget
entry = Text(root, height=33, width=72, wrap=WORD)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Attach the scrollbar to the text widget
entry.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=entry.yview)

root.mainloop()
