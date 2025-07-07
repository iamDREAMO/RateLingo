from tkinter import *

myroot = Tk()   # Creating blank tkinter widow
myroot.geometry('300x300+500+400')

mybtn = Button(myroot, text= 'OWUSU')
mybtn.pack(side= TOP, padx = 5, pady = 5)
myroot.mainloop()