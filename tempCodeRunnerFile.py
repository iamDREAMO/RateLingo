from  tkinter import *

class Scrollbar_Canvas(Tk):
    def __init__(self):
        super().__init__()
        
        mycanvas = Canvas(self, width=150, height = 50)
        mycanvas.create_oval(30, 30, 90, 90, fill='Magenta')
        mycanvas.create_oval(300, 300, 380, 380, fill='Brown')
        mycanvas.grid(row=0,column=0)
        
        myscroll_x =Scrollbar(self, orient=HORIZONTAL, command=mycanvas.xview)
        myscroll_x.grid(row=1, column=0, sticky=EW) 
        myscroll_y = Scrollbar(self, command=mycanvas.yview)
        myscroll_y.grid(row=0,column=1,sticky=NS)
        
        mycanvas.config(scrollregion=mycanvas.bbox('all'))
        
if __name__ =='__main__':
    root = Scrollbar_Canvas()
    root.geometry('300x250')
    root.mainloop() 