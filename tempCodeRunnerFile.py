from tkinter import * 
root = Tk()
root.geometry('350x200')
root.title('SpinBox with Disabled Clicking')

# spinbox creation
spin1 = Spinbox(font= ('Cambria', 14, 'bold'), values=(10,35,49,50,60,23), state='readonly')
spin1.pack(pady=10)
root.mainloop()