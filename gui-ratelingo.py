# Test sample with Tkinter
#import tkinter
#tkinter._test()

# Building Basic GUI Program
from tkinter import * # type: ignore

# Resizing/Class
myroot = Tk()   # Creating an object of Tk class
myroot.resizable(width = True, height = True)   # Resize option for width/height 
myroot.mainloop()


# ATTRIBUTES

# DIMENSIONS:
# Borderwidth
from tkinter import * # type: ignore

myroot = Tk() 
myl1 = Label(myroot, text = 'Label1', bd = 5, relief = 'groove')   # borderwidth feature
myl1.pack()
myroot.mainloop()


# Highlighttickness, padX, padY
from tkinter import * # type: ignore

myroot = Tk() 
myb1 = Button(myroot, text = 'Without HT')   # No Hihlighttickness feature
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With HT', highlightthickness=10)   # Hihlighttickness feature
myb2.grid(row=1, column=1, padx=10, pady=10)   # With padX and padY
myroot.mainloop()


# Wraplength
from tkinter import * # type: ignore
myroot = Tk()
myl1 = Label(myroot, text = 'KOFI', wraplength=2)   # with wrplength
myl1.pack()
myl2 = Label(myroot, text = 'AMAZING', wraplength=0)
myl2.pack()
myroot.mainloop()


# Height, Underline, Width
from tkinter import * # type: ignore
myroot = Tk()
myl1 = Label(myroot, text = 'BENEDICT', width=15, height=4, underline=3, font=('Cambria', 14))
myl1.pack()
myroot.mainloop()


# COLORS:
# Activebackground, background
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, activebackground= "Magenta2", bg = '#FFC000', text= 'DREAMO')
myb1.pack()
myroot.mainloop()  


# Activeforeground, foreground
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, activeforeground= 'Cyan2', fg= 'Salmon', text= 'GHANA')
myb1.pack()
myroot.mainloop()


# Disabledforeground
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, state = 'disabled', text = 'BONO', disabledforeground= 'red')
myb1.pack()
myroot.mainloop()


# Highlightbackground
from tkinter import * # type: ignore
myroot = Tk()
mye1 = Entry(myroot, bg= 'Cyan3', highlightthickness=10, highlightbackground= 'Slateblue1', highlightcolor= 'Black')
mye1.pack(padx= 5, pady=5)
mye2 = Entry(myroot)
mye2.pack()
mye2.focus()
myroot.mainloop()


# Selectbackground, selectforeground
from tkinter import * # type: ignore
myroot = Tk()
str1 = StringVar()
mye1 = Entry(myroot, selectbackground='OliveDrab1', selectforeground= 'Deep Pink', textvariable= str1)
mye1.pack()
str1.set('TREDE')
myroot.mainloop()


# FONTS
from tkinter import * #type: ignore
from tkinter.font import Font
myroot = Tk()

myfont1 = Font(family= 'Helvetica', size= 14, weight='bold', underline= 0, slant = 'roman', overstrike= 0) # type: ignore
myl1= Label(myroot, text = 'BENEDICT', font = myfont1)
myl1.pack() # for displaying the label

myroot.mainloop() # display the window until we press the close button (x)
 

# Viewing the Font family
from tkinter import * # type: ignore # Importing module
from tkinter import font
myroot = Tk() # window creation and initialize the interpreter

myfont_list = list(font.families())
for loop in myfont_list:
    print(loop,end = ',')
    
myroot.mainloop()

# Using tuple to access the font family
from tkinter import * # type: ignore
from tkinter.font import Font
myroot = Tk()

myl1 = Label(myroot, text = 'DREAMO', font = ('Arial', '18', 'bold roman underline')) # type: ignore
myl1.pack()
myroot.mainloop()


# ANCHORS (N.S,E,W,NE,NW,SE,SW,CENTER)
from tkinter import * # type: ignore
myroot = Tk()
myroot.geometry('200x200')

# Choose anchor and code remains the same
myl1 = Label(myroot, text= 'KOTEI', anchor= CENTER, font =('Arial', '20', 'bold roman'), bd = 2, relief = 'raised', width = 10, height = 6) # type: ignore
myl1.pack()
myroot.mainloop()


# RELIEF STYLES
from tkinter import * # type: ignore

myroot = Tk()
myroot.geometry('300x200')
myb1 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= FLAT, bd =5)
myb1.pack()
myb2 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= GROOVE, bd =5)
myb2.pack()
myb3 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= SUNKEN, bd =5)
myb3.pack()
myb4 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= RAISED, bd =5)
myb4.pack()
myb5 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= RIDGE, bd =5)
myb5.pack()
myroot.mainloop()


# BITMAPS
from tkinter import *  # type: ignore

myroot = Tk()
myroot.geometry('300x350')
myb1 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'error', bd = 4)
myb1.pack()
myb2 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'info', bd = 4)
myb2.pack()
myb3 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'warning', bd = 4)
myb3.pack()
myb4 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'question', bd = 4)
myb4.pack()
myroot.mainloop()


# CURSORS
from tkinter import *

myroot = Tk()
myroot.geometry('250x250')
myb4 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'arrow', bd = 4)
myb4.pack()
myb5 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'cross', bd = 4)
myb5.pack()
myb6 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'spider', bd = 4)
myb6.pack()
myb7 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'star', bd = 4)
myb7.pack()
myroot.mainloop()