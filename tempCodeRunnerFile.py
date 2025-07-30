from tkinter import *
root = Tk()

def click():
    text1.insert('insert',"<>")
    
btn = Button(root, text='Click Here!', command=click)
btn.pack()

text1 = Text(root, width=55, height=30)
text1.pack()

def insertimage():
    text1.image_create('insert', image = image1)

image1 = PhotoImage(file='Add-icon.png')
btn1 = Button(root, text='CreateImage', command=insertimage)
btn1.pack(pady=10)
root.mainloop()