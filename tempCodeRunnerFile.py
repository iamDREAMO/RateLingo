from tkinter import *
from tkinter.ttk import *

myroot =Tk()
myroot.geometry('200x200')
myroot.title('CheckButton Widget')

def myget():
    if i2.get() == 'Check':
        s1.set('Checked')
    else:
        s1.set('Unchecked')
        
i2 = StringVar()
myc2 = Checkbutton(myroot, text= 'Check/Uncheck', variable = i2, offvalue= 'Uncheck', onvalue= 'Check', command= myget)
myc2.pack()

s1 = StringVar()
mye1 = Entry(myroot, font= ('Cambria', 14, 'bold'), textvariable= s1)
mye1.pack(pady=10)

myroot.mainloop()