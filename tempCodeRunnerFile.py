
from tkinter import *

class MyLabelFrame(Tk):
    def __init__(self):
        super().__init__()
        
        # assigned text for display in LabelFrame 
        self.lf1 = LabelFrame(self, text= 'Welcome to LabelFrame and ButtonFrame',
                              font=('Arial', 13, 'bold'), bg ='LightBlue')
        self.lf1.pack(fill='both', expand='yes')
        
        # create and define label
        self.l1 = Label(self.lf1, text= 'This is a Label', bg='Pink')
        self.l1.pack(side=TOP)
        
        # create and define button
        self.btn = Button(self.lf1, text= 'This is a Button', bg='Brown')
        self.btn.pack(side=LEFT) 
        
        # create and assign text to LableFrame
        self.lf2 = LabelFrame(self, text= 'Welcome to CheckButton and RadioButton Frame',
                              font=('Arial', 13, 'bold'), bg ='LightGreen')
        self.lf2.pack(fill='both', expand='yes')
        
        # create and define CheckButton
        self.chkb = Checkbutton(self.lf2, text= 'This is a CheckButton', bg='Yellow')
        self.chkb.pack(side=RIGHT) 
        
        # create and define RadioButton
        self.rabtn = Radiobutton(self.lf2, text= 'This is a RadiokButton', bg='Cyan')
        self.rabtn.pack(side=BOTTOM) 

if __name__ == '__main__':
    root = MyLabelFrame()
    root.geometry('400x200')
    root.mainloop()