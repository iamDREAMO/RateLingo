from tkinter import *
myroot = Tk()
myroot.title('Car Selection')
myroot.geometry('300x300')

myvar = StringVar() # tk variable created
myvar.set('Cars')

# create an option menu by passing the variable and option list
myselection = OptionMenu(myroot, myvar, 'BMW', 'Benz', 'Ford', 'Kia', 'Toyota') # variable bound to option menu
myselection.pack()

# create button with command
def mydisplay():
    print('The chosen car :', myvar.get())
    
mybtn = Button(myroot, text= 'My Choice',command=mydisplay)
mybtn.pack(pady=30, side= BOTTOM, anchor= N)

myroot.mainloop()