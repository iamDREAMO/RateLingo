from tkinter import *
class MyleftRightMouseClick(Tk):
    def __init__(self):
        super().__init__()
        self.title('Button Left and Right click')
        
        def mycall(event):
            print('Left Clicked')
            
        def mycallme(event):
            print('Right Clicked')
            
        self.myb1 = Button(self, text = 'LeftClick', font = ('Cambria', 14))
        self.myb1.bind('<Button-1>', mycall) # Left click
        self.myb1.pack(pady= 10) # for displaying the button
        
        self.myb2 = Button(self, text = 'RightClick', font= ('Cambria', 14))
        self.myb2.bind('<Button-3>', mycallme) # Right Click
        self.myb2.pack(pady=10) # for displaying the button
        
if __name__ == '__main__':
    myroot = MyleftRightMouseClick()
    myroot.geometry('400x250')
    myroot.mainloop() 