# specify set of values in spinbox
from tkinter import *
root = Tk()
root.geometry('200x200')
root.title('SpinBox Values Specified')

# creation of spinbox
spin1 = Spinbox(font= ('Cambria', 14, 'bold'), values=(10,15,20,25,30), bd=10, relief= RIDGE)
spin1.pack()
root.mainloop()