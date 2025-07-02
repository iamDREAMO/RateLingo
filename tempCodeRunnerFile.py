from tkinter import *
from tkinter.font import Font
myroot = Tk()

myfont1 = Font(family= 'Helvetica', size= 14, weight='bold', underline= 0, slant = 'roman', overstrike= 0)
myl1= Label(myroot, text = 'BENEDICT', font = myfont1)
myl1.pack()

myroot.mainloop()
