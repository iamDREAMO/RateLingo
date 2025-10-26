from tkinter import *
root = Tk()
root.title('Trace_add')
root.geometry('300x300')
value = StringVar()

btn1 = Button(root, textvariable = value, bg = 'Magenta')
btn1.pack(padx = 20, pady = 20)

ent1 = Entry(root, textvariable = value, bg = 'Cyan')
ent1.pack(padx = 20, pady = 20)

# define the callback function
def attachedcallback(var, indx, mode):
    print("Traced variable{}: ".format(value.get()))
    
# register the observer
value.trace_add('write', attachedcallback)
root.mainloop()