from tkinter import *

root = Tk()
root.geometry('200x200')
root.title('SpinBox')

# spinbox creation
spin = Spinbox(font=('Cambria', 14, 'bold'), from_=10, to=20)
spin.pack()
root.mainloop()