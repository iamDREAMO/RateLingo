from tkinter import *
myroot = Tk()
myroot.geometry('200x200')

# Choose anchor and code remains the same
myl1 = Label(myroot, text= 'KOTEI', anchor= CENTER, font =('Arila', '20', 'bold roman'), bd = 2, relief = 'raised', width = 10, height = 6)
myl1.pack()
myroot.mainloop()