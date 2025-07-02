from tkinter import *
myroot = Tk()
str1 = StringVar()
mye1 = Entry(myroot, selectbackground='OliveDrab1', selectforeground= 'Deep Pink', textvariable= str1)
mye1.pack()
str1.set('TREDE')
myroot.mainloop()
