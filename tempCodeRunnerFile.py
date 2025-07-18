from tkinter import *
myroot = Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

num = 1
def mydisplay(e):
    global num
    num = num + 1
    if num%2 == 0:
        myroot.configure(background='LightBlue')
    else:
        myroot.configure(background='Brown')
        
mybtn1 = Button(myroot, text= 'Click Here!!!', font=('Cambria', 15, 'bold'))
mybtn1.bind('<Button>', mydisplay) # on mouse pressing button
mybtn1.bind('<ButtonRelease>', mydisplay) # on mouse releasing button
mybtn1.pack()

myroot.mainloop()