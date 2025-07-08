from tkinter import *
from tkinter import messagebox

class MyJustify(Tk):
    def __init__(self):
        super(). __init__()
        self.title('Justify in Button')
        
        def mycenterjustify():
            messagebox.showinfo('Justify', 'Justify CENTER')
            
        def myleftjustify():
            messagebox.showinfo('Justify', 'Justify LEFT')
            
        def myrightjustify():
            messagebox.showinfo('Justify', 'Justify RIGHT')
            
        # Default justify in CENTER
        mybtn1 = Button(self, text= 'JUSTIFY\nCENTER\nCENTER CENTER', bd= 3, relief = 'groove', font= ('Cambria', 13), width = 20, height = 3, command = mycenterjustify)
        mybtn1.pack(pady= 10, side = BOTTOM)
        
        mybtn2 = Button(self, text= 'JUSTIFY\nLEFT\nLEFT LEFT', bd= 3, relief = 'groove', font= ('Cambria', 13), justify= LEFT, width = 20, height = 3, command = myleftjustify)
        mybtn2.pack(pady= 10, side = RIGHT)
        
        mybtn3 = Button(self, text= 'JUSTIFY\nRIGHT\nRIGHT RIGHT', bd= 2, font= ('Cambria', 13), justify= RIGHT, width = 20, height = 3, command = myrightjustify)
        mybtn3.pack(side = TOP)
        
if __name__ == "__main__":
    myroot = MyJustify()
    myroot.geometry('350x350')
    myroot.mainloop()