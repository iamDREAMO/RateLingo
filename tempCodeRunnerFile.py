from tkinter import *

class Just1(Tk):
    def __init__(self):
        super().__init__()
        self.title('Justify the Label')
        lab1 = Label(self, text= 'KOFI')
        lab1.pack()
        lab2 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12))
        
        # default justify is CENTER
        lab2.pack()
        lab3 = Label(self, text= 'KOFI')
        lab3.pack()
        lab4 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12), justify = LEFT)
        lab4.pack()
        lab5 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12), justify = RIGHT)
        lab5.pack()
        
if __name__ == '__main__':
    root = Just1()
    root.geometry('350x300')
    root.mainloop()