from tkinter import *
root = Tk()
root.geometry()
root.title('Text Widget')

#creating the text widget
text1 = Text(root, width=18, height=10, font=('Cambria', 12, 'bold'), wrap =WORD, 
             padx=10, pady=10, bd=4, selectbackground='Grey', selectforeground='Black')
text1.pack()
root.mainloop()
