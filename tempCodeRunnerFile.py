from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('300x200')
root.title('Text in Combobox')

str_val = StringVar()

def display():
    str_val = combo.get()
    print(str_val)
    
list1 = ['Ghana','Togo','Algeria','Morocco']
str_val.set('Ghana')

combo = Combobox(root, values= list1, height=5, textvariable=str_val, postcommand=display)
combo.pack()

root.mainloop()