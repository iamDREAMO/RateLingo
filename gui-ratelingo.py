# Test sample with Tkinter
#import tkinter
#tkinter._test()

# Building Basic GUI Program
from tkinter import *

# Resizing/Class
myroot = Tk()   # Creating an object of Tk class
myroot.resizable(width = True, height = True)   # Resize option for width/height 

myroot.mainloop()


# Lables
from tkinter import *

myroot = Tk() 
myl1 = Label(myroot, text = 'Label1', bd = 5, relief = 'groove')   # Lable feature
myl1.pack()

myroot.mainloop()

# Highlighttickness
from tkinter import *

myroot = Tk() 
myb1 = Button(myroot, text = 'Without HT')   # Hihlighttickness feature
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With HT', highlightthickness=10)
myb2.grid(row=1, column=1, padx=10, pady=10)

myroot.mainloop()
