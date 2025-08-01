from tkinter import *

class LabelPosition(Tk):
    def __init__(self):
        super().__init__()
        self.title('Position Text within a Label')
        self.label1 = Label(self, text = 'Hello! \n Welcome!', bd=4, relief = SUNKEN, 
                           font= 'Hevectica 14', width=10, height=4, anchor= SW)
        self.label1.pack()
        
if __name__ == '__main__':
    root = LabelPosition()
    root.mainloop()