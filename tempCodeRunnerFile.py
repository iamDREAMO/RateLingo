from tkinter import *

class Scrollbar_Entry(Tk):
    def __init__(self):
        super().__init__()
        self.sclhbar = Scrollbar(self, orient=HORIZONTAL)
        self.sclhbar.pack(side = BOTTOM, fill=X)
        
        self.mye1 = Entry(self, xscrollcommand=self.sclhbar.set) # creation of entry horizontal scrollbars attached
        self.mye1.pack(expand=0, fill=BOTH)
        
        # horizontal elements
        for loop in range(30): # insertelements from 0 to 29 in the listbox
            self.mye1.insert(END, str(loop) + '\t')
            
            self.sclhbar.config(command=self.mye1.xview)
            
if __name__=='__main__':
    root = Scrollbar_Entry()
    root.geometry('300x100')
    root.mainloop()