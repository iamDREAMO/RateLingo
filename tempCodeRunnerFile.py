from tkinter import *
root = Tk()
root.geometry('300x300')

# StringVar Variable
stv = StringVar()

# display function
def display():
    root.configure(bg= stv.get())
    
# creation of spinbox
spin = Spinbox(font= ('Cambria', 14, 'bold'), command=display,
               values= ['Red', 'Green', 'Blue', 'Pink', 
                        'Magenta', 'Yellow'], textvariable=stv)
spin.pack()
root.mainloop()