from tkinter import *

root = Tk()
root.geometry('200x150')
root.title('StatusBar_Example')

statusbar = Label(root, text='Example of StatusBar...', 
                  bd=1, relief=GROOVE, anchor=W) # for text aliginment within label

statusbar.pack(side=BOTTOM, fill=X) 
root.mainloop()
