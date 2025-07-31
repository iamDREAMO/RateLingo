# Getting Insights of Display Widgets in tkinter
from tkinter import *
root = Tk()

root.maxsize(300,300) # maximum size of the window set up to 300 only
root.resizable(0,0) # fixed window size

label1 = Label(root, text= 'Tkinter\nis\nAwesome', font=('Cambria', 18, 'bold'),
               bg= 'Cyan', fg= 'Black', width= '16', height= '4')
label1.pack()
root.mainloop()