from tkinter import *

class AccessOptions(Tk):
    def __init__(self):
        super().__init__()
        self.title('Access tkinter label options')
        lab1 = Label(self, text= 'Stay\nSafe From\nFrom Smoking', bd = 2,
                     bg= 'Cyan', relief = 'solid', font= ('Cambria', 12, 'bold'),
                     width= 20, height= 4, anchor = NW, justify = LEFT)
        lab1.pack()
        print(lab1['text'])
        print('-------')
        print(lab1['bd'])
        print(lab1['font'])
        print(lab1['width'])
        print(lab1['height'])
        print(lab1['anchor'])
        print(lab1['justify'])
        
if __name__ == '__main__':
    root = AccessOptions()
    root.geometry('300x200')
    root.mainloop()