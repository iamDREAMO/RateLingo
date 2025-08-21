from tkinter import *
root = Tk()
Str1 = StringVar()

# message widget object
msg1 = Message(root, textvariable= Str1, relief=SUNKEN, font =('Arial', 12,'bold'),
               fg = 'Cyan', bg = 'Brown')
Str1.set('Display of string message')
msg1.pack()
root.geometry('200x200')
root.mainloop()
    