from tkinter import *
myroot = Tk() 
myroot.geometry('500x500')

mybtn_height =Button(myroot, text='60px high')
mybtn_height.place(height= 100, x=300, y=300)

myroot.mainloop()