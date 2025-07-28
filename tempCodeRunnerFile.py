from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x300')
root.title('Text_Widget Content')

# Text widget creation
txt = Text(root, width=18, height=12, 
           font=('Arial', 12), wrap = WORD,
           padx=10, pady=10, bd=4, 
           selectbackground='Grey', selectforeground='Blue')
txt.pack()

# inserting text in the text widget
txt.insert('1.0', 'Beginner! Welcome to learning tkinter text widget. \n This is for multiple lines.')

# callback function
def myget():
    messagebox.showinfo('Text widget contents are: ',
                        txt.get('1.0', 'end')) # reading the entire content displaying
    
btn = Button(root, text='Read', command=myget)
btn.pack()
root.mainloop() 