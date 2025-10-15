from tkinter import *
root =Tk()
root.geometry('300x300')

# first paned window object
pw = PanedWindow(root)
pw.pack(fill=BOTH, expand= 1)

ent = Entry(pw, bd=5, relief='groove', font =('Arial', 12), bg='LightGreen')
pw.add(ent)

# second paned window widget
pw1 = PanedWindow(pw, orient=VERTICAL)
pw.add(pw1) # add second paned window to first paned window

ent1 = Spinbox(pw1, from_=10, to= 20, font =('Helvetica', 12), bg='LightBlue')
pw.add(ent)

ent2 = Entry(pw1, bg ='brown', relief='sunken',font =('Arial', 12))
ent2.insert(0,3) # set value to 3

pw.configure(sashrelief= RAISED) # show sash

# subtraction function
def subtract():
    num1 = int(ent1.get()) # get value of spinbox
    num2 = int(ent2.get()) # get value of entry
    data1 = str(num1-num2)
    ent.insert(1, data1)
    
# add spinbox to second paned window
pw1.add(ent1)

# add entry to second paned window
pw1.add(ent2)

# create button widget
btn = Button(pw1, text='Subtract', command=subtract)

# add button to second paned window
pw1.add(btn)

root.mainloop()