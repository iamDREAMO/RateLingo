from tkinter import *
from tkinter import messagebox
myroot = Tk()

def mydisplay():
    messagebox.showinfo('Message', 'Hey Kofi!')
    
mybtn = Button(myroot, text= 'Display', font= ('Cambria', 13, 'bold',), command= mydisplay)
mybtn.pack(padx= 20, pady= 30)
myroot.mainloop()