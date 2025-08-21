from tkinter import *

class StrVartext(Tk):
    def __init__(self):
        super().__init__()
        self.vall = StringVar()
        self.title('StringVar/textvariable as Tk label')
        self.lab1 = Label(self, font =('Cambria', 12, 'bold'),
                          textvariable = self.vall, relief = 'groove')
        self.lab1.pack()
        self.vall.set('Tkinter is great')
        
if __name__ == '__main__':
    root = StrVartext()
    root.geometry('300x300')
    root.mainloop()
    