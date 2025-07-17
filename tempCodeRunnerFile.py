from tkinter import *
myroot =Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

# using lambda expression
myshow1 = lambda e: myroot.configure(background= 'Cyan')
myshow2 = lambda e: myroot.configure(background='Blue')
myshow3 = lambda e: myroot.configure(background= 'LightGreen')

mytk_btn1 = Button(myroot, text='Background Colour', font=('Cambria', 14, 'bold'), fg='Brown')
mytk_btn1.bind('<Button-1>', myshow1) # left key of mouse
mytk_btn1.bind('<Button-2>', myshow2) # wheel key mouse
mytk_btn1.bind('<Button-3>', myshow3) # right key of mouse
mytk_btn1.pack()

myroot.mainloop()