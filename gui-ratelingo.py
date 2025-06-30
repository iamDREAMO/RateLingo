# Test sample with Tkinter
#import tkinter
#tkinter._test()

# Building Basic GUI Program
from tkinter import *

myroot = Tk()     # creating an object of Tk class
myroot.resizable(width = True, height = True) # resize option for width/height
myl1 = Label(myroot, text = 'Label1', bd = 8, relief = 'groove') # labelling feature
myl1.pack()

myroot.mainloop()

