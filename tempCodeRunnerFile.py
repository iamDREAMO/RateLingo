from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('300x200')
root.title('Combobox Widget')

# List of values
List1 = list(range(1,10))

combo = Combobox(root, values=List1, width=15)
combo.pack(padx=40, pady=10) 
root.mainloop()