from tkinter import *
myroot = Tk()   # creating an oblject of Tk class -- object of window

myroot.geometry('200x200') # window can be resized to any size until we use root.resizeable
myroot.resizable(0,0)   # window size is fixed (cannot be larger/smaller)

mystr = StringVar() # S1
print(type(mystr))  # S2
my_entry = Entry(myroot, font = ('Cambria, 13'), textvariable = mystr)
my_entry.pack()

def myshow():
    mydata = mystr.get() #S3
    print(mydata)
    mystr.set('') # S4
    
my_btn = Button(myroot, font = ('Cambria', 13), text= 'Get Data', command= myshow)
my_btn.pack()

myroot.mainloop()