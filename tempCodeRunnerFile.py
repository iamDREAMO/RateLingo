from tkinter import *

myroot = Tk() 
myb1 = Button(myroot, text = 'Without HT')   # Hihlighttickness feature
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With HT', highlightthickness=10)
myb2.grid(row=1, column=1, padx=10, pady=10)

myroot.mainloop()