from tkinter import *

myroot = Tk()
myroot.geometry('300x200')

num1 = BooleanVar()
mystr = StringVar()

def mydatainsertion():
    if num1.get() == True:
        mystr.set('It is set to True')
    else:
        mystr.set('It is set to False')
        
myc1 = Checkbutton(myroot, variable= num1, font = ('Cambria', 13), text= 'DREAMO', command= mydatainsertion)
myc1.pack()

mye1 = Entry(myroot, width= 20, textvariable= mystr)
mye1.pack()

myroot.mainloop() 