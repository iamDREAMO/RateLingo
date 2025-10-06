from tkinter import *

root = Tk()
root.geometry('300x300')

frame1=Frame(root, width=150,height=150, bg='Red')
frame1.grid(row=0, column=0)

frame2=Frame(root, width=150,height=150, bg='Green')
frame2.grid(row=1, column=0)

frame3=Frame(root, width=150,height=150, bg='Blue')
frame3.grid(row=0, column=1)

frame4=Frame(root, width=150,height=150, bg='Cyan')
frame4.grid(row=1, column=1)

root.mainloop()