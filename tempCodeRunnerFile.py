from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('Frame Input')

frame1=Frame(root)
l1= Label(frame1, text = 'Name')
l1.grid(row=0, column=0)
l2= Label(frame1, text = 'Age')
l2.grid(row=1, column=0)
l3= Label(frame1, text = 'Contact')
l3.grid(row=2, column=0)

ent1 = Entry(frame1)
ent1.grid(row=0, column=1)
ent2 = Entry(frame1)
ent2.grid(row=1, column=1)
ent3 = Entry(frame1)
ent3.grid(row=2, column=1)

btn = Button(frame1, text= 'View')
btn.grid(row=3, columnspan= 2)
frame1.grid(row=3, column=0)

root.mainloop()