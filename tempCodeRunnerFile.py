from tkinter import *

class Scrollbar_Text(Tk):
    def __init__(self):
        super().__init__()
        
        self.mysclbar = Scrollbar(self) # scrollbar creation and attaching to the main window
        self.mysclbar.pack(side=RIGHT, fill=Y) # scrollbar added to window right side
        
        self.sclhbar =Scrollbar(self, orient=HORIZONTAL)
        self.sclhbar.pack(side=BOTTOM, fill=X)
        
        self.mytext = Text(self, width=600, height=600, 
                           yscrollcommand=self.mysclbar.set,
                           xscrollcommand=self.sclhbar.set,
                           wrap=NONE) # creation of textbox ad both horizontal/vertical scrillbars are attached to the textbox
        self.mytext.pack(expand=0, fill=BOTH)    
        
        # horizontal elements
        for loop in range(30): # insertelements from 0 to 49 in the text
            self.mytext.insert(END, str(loop) + '\t')
            
        # vertical elements
        for loop in range(50): # insertelements from 0 to 49 in the text
            self.mytext.insert(END, str(loop) + '\n')
            
        self.sclhbar.config(command=self.mytext.xview) # for need of horizontal view settings scrollbar command option to textbox.xview method
        self.mysclbar.config(command=self.mytext.yview) # for need of horizontal view settings scrollbar command option to textbox.yview method
        
if __name__ == '__main__':
    root = Scrollbar_Text()
    root.geometry('300x300')
    root.mainloop()    