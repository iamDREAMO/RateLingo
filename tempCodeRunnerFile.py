from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0)

myroot.bind('<Key-a>', lambda e: myroot.configure(background='LightBlue')) # on pressing key 'a'
myroot.bind('<Key-b>', lambda e: myroot.configure(background='LightGreen')) # on pressing key 'b'
myroot.bind('<Key-c>', lambda e: myroot.configure(background='Pink')) # on pressing key 'c'

myroot.mainloop()