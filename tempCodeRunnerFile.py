from tkinter import *
myroot =Tk()
myroot.geometry('350x250')
myroot.title('Checkbutton Widget')

mynum1 = IntVar()
mynum2 = IntVar()
mys1 = StringVar()

def mydatainsertion():
    if mynum1.get() == 1 and mynum2.get() == 0: # read status of checkbutton
        mys1.set('DREAMO') # setting the value to  the  Entry widget
        
    if mynum1.get() == 0 and mynum2.get() == 1:
        mys1.set('Ben.COM')
        
    if mynum1.get() == 1 and mynum2.get() == 1:
        mys1.set('I am there no matter what!')
        
    if mynum1.get() == 0 and mynum2.get() == 0:
        mys1.set('I want to see both')
        
myc1 = Checkbutton(myroot, variable= mynum1, font = ('Cambria', 14, 'bold'), text='DREAMO', command=mydatainsertion)
myc1.pack()

myc2 = Checkbutton(myroot, variable= mynum2, font=('Cambria', 14, 'bold'), text='Ben.COM', command=mydatainsertion)
myc2.pack()

mye1 = Entry(myroot, font= ('Cambria', 14), textvariable=mys1)
mye1.pack()

myroot.mainloop()
