from tkinter import *
root = Tk()

text1 = 'This session is to test my knowledgr so far with tkinter'
msg1 = Message(root, text=text1, font =('Cambria', 12, 'bold'),
               fg="Blue", bg='Magenta', relief= RAISED)
msg1.pack()
root.geometry('200x200')
root.mainloop()