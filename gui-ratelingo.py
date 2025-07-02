# Test sample with Tkinter
#import tkinter
#tkinter._test()

# Building Basic GUI Program
from tkinter import *

# Resizing/Class
myroot = Tk()   # Creating an object of Tk class
myroot.resizable(width = True, height = True)   # Resize option for width/height 
myroot.mainloop()


# ATTRIBUTES

# DIMENSIONS:
# Borderwidth
from tkinter import *

myroot = Tk() 
myl1 = Label(myroot, text = 'Label1', bd = 5, relief = 'groove')   # borderwidth feature
myl1.pack()
myroot.mainloop()


# Highlighttickness, padX, padY
from tkinter import *

myroot = Tk() 
myb1 = Button(myroot, text = 'Without HT')   # No Hihlighttickness feature
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With HT', highlightthickness=10)   # Hihlighttickness feature
myb2.grid(row=1, column=1, padx=10, pady=10)   # With padX and padY
myroot.mainloop()


# Wraplength
from tkinter import *
myroot = Tk()
myl1 = Label(myroot, text = 'KOFI', wraplength=2)   # with wrplength
myl1.pack()
myl2 = Label(myroot, text = 'AMAZING', wraplength=0)
myl2.pack()
myroot.mainloop()


# Height, Underline, Width
from tkinter import *
myroot = Tk()
myl1 = Label(myroot, text = 'BENEDICT', width=15, height=4, underline=3, font=('Cambria', 14))
myl1.pack()
myroot.mainloop()


# COLORS:
# Activebackground, background
from tkinter import *
myroot = Tk()
myb1 = Button(myroot, activebackground= "Magenta2", bg = '#FFC000', text= 'DREAMO')
myb1.pack()
myroot.mainloop()  


# Activeforeground, foreground
from tkinter import *
myroot = Tk()
myb1 = Button(myroot, activeforeground= 'Cyan2', fg= 'Salmon', text= 'GHANA')
myb1.pack()
myroot.mainloop()


# Disabledforeground
from tkinter import *
myroot = Tk()
myb1 = Button(myroot, state = 'disabled', text = 'BONO', disabledforeground= 'red')
myb1.pack()
myroot.mainloop()

# Highlightbackground
from tkinter import *
myroot = Tk()
mye1 = Entry(myroot, bg= 'Cyan3', highlightthickness=10, highlightbackground= 'Slateblue1', highlightcolor= 'Black')
mye1.pack(padx= 5, pady=5)
mye2 = Entry(myroot)
mye2.pack()
mye2.focus()
myroot.mainloop()

