from tkinter import *

class MyBtnTextWithImage(Frame):
    def __init__(self, root = None):
        Frame.__init__(self, root)
        self.root = root
        self.myphoto = PhotoImage(file = 'Add-icon2.png')
        self.mybtn1 = Button(self.root, image = self.myphoto, text = 'Hey!', compound=LEFT)
        self.mybtn1.pack(padx= 10, pady= 10)
        self.mybtn2 = Button(self.root, image = self.myphoto, text='Hey!', compound= RIGHT)
        self.mybtn2.pack(padx= 10, pady=10)
        self.mybtn3 = Button(self.root, image = self.myphoto, text= 'Hey!', compound=TOP)
        self.mybtn3.pack(padx=10, pady=10)
        self.mybtn4 = Button(self.root, image = self.myphoto, text= 'Hey!', compound= BOTTOM)
        self.mybtn4.pack(padx= 10, pady=10)
        
if __name__ == '__main__':
    myroot = Tk()
    myobj = MyBtnTextWithImage(myroot)
    myroot.title('Image Using Button')
    myroot.geometry('400x300')
    myroot.mainloop()