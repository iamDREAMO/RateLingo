from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Tag to Text_Wigdet')

text = Text(root, width=18, height=10, font=('Cambria', 14, 'bold'), wrap=WORD, padx=10,
            pady=10, bd=4, selectbackground='Blue', selectforeground='Green')
text.pack()

text.insert('1.0', 'This is the First line')
text.insert('1.0 + 1 line', '\nThis is Second Line')
text.insert('1.0 + 2 lines', '\nThis is the Third Line')

# 1st par: Name of the tag which  will be created as a string
# 2nd par: start
# 3rd pas: end
text.tag_add('Tag', '1.0', '1.0 wordend')

# Confir=guring the properties about the tag
text.tag_configure('Tag', background='Brown')
root.mainloop()