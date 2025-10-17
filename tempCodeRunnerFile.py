from tkinter import *
root = Tk()
root.geometry('400x400')
root.title('Menu_With_Checkbutton')

# create menubutton
menubutton = Menubutton(root, text= 'Foods', font=('Cambria', 12, 'bold'),
                       justify=CENTER, relief='groove')
menubutton.grid()

# create pull down menu
menubutton.menu = Menu(menubutton, tearoff = 0)
menubutton['menu'] = menubutton.menu

# create checkbutton
menubutton.menu.add_checkbutton(label = 'Anwamoo', font=('Cambria', 12, 'bold'),
                                variable = IntVar())
menubutton.menu.add_checkbutton(label = 'Jollof', font=('Cambria', 12, 'bold'),
                                variable = IntVar())
menubutton.menu.add_checkbutton(label = 'Waakye', font=('Cambria', 12, 'bold'),
                                variable = IntVar())
menubutton.pack()
root.mainloop()