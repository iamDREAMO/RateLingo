# Test sample with Tkinter
#import tkinter
#tkinter._test()

# Building Basic GUI Program
from tkinter import * # type: ignore

# Resizing/Class
myroot = Tk()   # Creating an object of Tk class
myroot.resizable(width = True, height = True)   # Resize option for width/height 
myroot.mainloop()


# ATTRIBUTES

# DIMENSIONS:
# Borderwidth
from tkinter import * # type: ignore

myroot = Tk() 
myl1 = Label(myroot, text = 'Label1', bd = 5, relief = 'groove')   # borderwidth feature
myl1.pack()
myroot.mainloop()


# Highlighttickness, padX, padY
from tkinter import * # type: ignore

myroot = Tk() 
myb1 = Button(myroot, text = 'Without HT')   # No Hihlighttickness feature
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With HT', highlightthickness=10)   # Hihlighttickness feature
myb2.grid(row=1, column=1, padx=10, pady=10)   # With padX and padY
myroot.mainloop()


# Wraplength
from tkinter import * # type: ignore
myroot = Tk()
myl1 = Label(myroot, text = 'KOFI', wraplength=2)   # with wrplength
myl1.pack()
myl2 = Label(myroot, text = 'AMAZING', wraplength=0)
myl2.pack()
myroot.mainloop()


# Height, Underline, Width
from tkinter import * # type: ignore
myroot = Tk()
myl1 = Label(myroot, text = 'BENEDICT', width=15, height=4, underline=3, font=('Cambria', 14))
myl1.pack()
myroot.mainloop()


# COLORS:
# Activebackground, background
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, activebackground= "Magenta2", bg = '#FFC000', text= 'DREAMO')
myb1.pack()
myroot.mainloop()  


# Activeforeground, foreground
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, activeforeground= 'Cyan2', fg= 'Salmon', text= 'GHANA')
myb1.pack()
myroot.mainloop()


# Disabledforeground
from tkinter import * # type: ignore
myroot = Tk()
myb1 = Button(myroot, state = 'disabled', text = 'BONO', disabledforeground= 'red')
myb1.pack()
myroot.mainloop()


# Highlightbackground
from tkinter import * # type: ignore
myroot = Tk()
mye1 = Entry(myroot, bg= 'Cyan3', highlightthickness=10, highlightbackground= 'Slateblue1', highlightcolor= 'Black')
mye1.pack(padx= 5, pady=5)
mye2 = Entry(myroot)
mye2.pack()
mye2.focus()
myroot.mainloop()


# Selectbackground, selectforeground
from tkinter import * # type: ignore
myroot = Tk()
str1 = StringVar()
mye1 = Entry(myroot, selectbackground='OliveDrab1', selectforeground= 'Deep Pink', textvariable= str1)
mye1.pack()
str1.set('TREDE')
myroot.mainloop()


# FONTS
from tkinter import * #type: ignore
from tkinter.font import Font
myroot = Tk()

myfont1 = Font(family= 'Helvetica', size= 14, weight='bold', underline= 0, slant = 'roman', overstrike= 0) # type: ignore
myl1= Label(myroot, text = 'BENEDICT', font = myfont1)
myl1.pack() # for displaying the label

myroot.mainloop() # display the window until we press the close button (x)
 

# Viewing the Font family
from tkinter import * # type: ignore # Importing module
from tkinter import font
myroot = Tk() # window creation and initialize the interpreter

myfont_list = list(font.families())
for loop in myfont_list:
    print(loop,end = ',')
    
myroot.mainloop()

# Using tuple to access the font family
from tkinter import * # type: ignore
from tkinter.font import Font
myroot = Tk()

myl1 = Label(myroot, text = 'DREAMO', font = ('Arial', '18', 'bold roman underline')) # type: ignore
myl1.pack()
myroot.mainloop()


# ANCHORS (N.S,E,W,NE,NW,SE,SW,CENTER)
from tkinter import * # type: ignore
myroot = Tk()
myroot.geometry('200x200')

# Choose anchor and code remains the same
myl1 = Label(myroot, text= 'KOTEI', anchor= CENTER, font =('Arial', '20', 'bold roman'), bd = 2, relief = 'raised', width = 10, height = 6) # type: ignore
myl1.pack()
myroot.mainloop()


# RELIEF STYLES
from tkinter import * # type: ignore

myroot = Tk()
myroot.geometry('300x200')
myb1 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= FLAT, bd =5)
myb1.pack()
myb2 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= GROOVE, bd =5)
myb2.pack()
myb3 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= SUNKEN, bd =5)
myb3.pack()
myb4 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= RAISED, bd =5)
myb4.pack()
myb5 = Button(myroot, text= 'DREAMO', font = ('Roboto', 12), relief= RIDGE, bd =5)
myb5.pack()
myroot.mainloop()


# BITMAPS
from tkinter import *  # type: ignore

myroot = Tk()
myroot.geometry('300x350')
myb1 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'error', bd = 4)
myb1.pack()
myb2 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'info', bd = 4)
myb2.pack()
myb3 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'warning', bd = 4)
myb3.pack()
myb4 = Button(myroot, text = 'TREDE', relief= RIDGE, bitmap = 'question', bd = 4)
myb4.pack()
myroot.mainloop()


# CURSORS
from tkinter import * # type: ignore

myroot = Tk()
myroot.geometry('250x250')
myb4 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'arrow', bd = 4)
myb4.pack()
myb5 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'cross', bd = 4)
myb5.pack()
myb6 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'spider', bd = 4)
myb6.pack()
myb7 = Button(myroot, text = 'ADUSEI', relief= RAISED, cursor= 'star', bd = 4)
myb7.pack()
myroot.mainloop()


# Python Tkinter Geometry Management

# pack() options: fill, expand, side (FES)
from tkinter import * # type: ignore
myroot = Tk()
myroot.geometry('300x300')
myb1 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb1.pack(fill= NONE)
myb2 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb2.pack(fill = X, padx = 10, pady = 10)
myb3 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb3.pack(side = LEFT, fill = Y, padx = 10, pady = 10)
myb4 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb4.pack(side = TOP, fill = X, padx = 10, pady = 10 )
myb5 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb5.pack(side= BOTTOM, fill = X, padx = 10, pady= 10)
myb6 = Button(myroot, text = 'YAW', fg= 'pink', bg= 'blue')
myb6.pack(side= RIGHT, fill= BOTH, expand= 1, padx= 10, pady= 10)
myroot.mainloop()


# grid() options : CCPPIIRRS (column,columnspan,padx,pady,ipadx,ipady,row,rowspan,sticky)
from tkinter import * # type: ignore
myroot = Tk()

mybtn_col = Button(myroot, text= 'It is column no. 4')
mybtn_col.grid(row= 0, column=4)

mybtn_colspan = Button(myroot, text= 'The columnspan is 4')
mybtn_colspan.grid(row= 1, columnspan=4)

mybtn_padx = Button(myroot, text='padx of 5 from outside widget')
mybtn_padx.grid(row=2, padx=5)

mybtn_pady =Button(myroot, text='pady of 10 from outside the  widget')
mybtn_pady.grid(row=3, pady=10)

mybtn_ipadx = Button(myroot,text= 'ipadx of 5 from inside wodget border')
mybtn_ipadx.grid(row= 4, ipadx=10)

mybtn_ipady = Button(myroot,text= 'ipadx of 5 from inside wodget border')
mybtn_ipady.grid(row= 5, ipady=10)

mybtn_row = Button(myroot, text= 'It is Row No.7')
mybtn_row.grid(row=7)

mybtn_rowspan = Button(myroot, text= 'It is Rowspan of 3')
mybtn_rowspan.grid(row= 8, rowspan=3)

mybtn_sticky = Button(myroot, text= 'Hey! I am at North-West')
mybtn_sticky.grid(sticky=NE)

myroot.mainloop()


# place()
from tkinter import *
myroot = Tk() 
myroot.geometry('500x500')

mybtn_height =Button(myroot, text='60px high')
mybtn_height.place(height= 60, x=300, y=300)

mybtn_width = Button(myroot, text='70px wide')
mybtn_width.place(width=70, x=400, y=400)

mybtn_relheight = Button(myroot, text='relheight of 0.7')
mybtn_relheight.place(relheight=0.7)

mybtn_relwidth = Button(myroot, text='relwidth of 0.4')
mybtn_relwidth.place(relwidth=0.4)

mybtn_relx = Button(myroot, text='relx of 0.5')
mybtn_relx.place(relx=0.5)

mybtn_rely =Button(myroot, text='rely of 0.8')
mybtn_rely.place(rely=0.8)

mybtn_x = Button(myroot, text='X = 500px')
mybtn_x.place(x=500)

mybtn_y = Button(myroot, text='Y = 520px')
mybtn_y.place(y=500)

myroot.mainloop()


# Geometry Method In Tkinter
from tkinter import *

myroot = Tk()   # Creating blank tkinter widow
myroot.geometry('300x150')

mybtn = Button(myroot, text= 'OWUSU')
mybtn.pack(side= TOP, padx = 5, pady = 5)
myroot.mainloop()

# Changing the position of the window
from tkinter import *

myroot = Tk()   # Creating blank tkinter widow
myroot.geometry('300x150+400+400')

mybtn = Button(myroot, text= 'OWUSU')
mybtn.pack(side= TOP, padx = 5, pady = 5)
myroot.mainloop()


# Inbuilt Variable Classes

# SringVar()
from tkinter import *
myroot = Tk()   # creating an oblject of Tk class -- object of window

myroot.geometry('200x200') # window can be resized to any size until we use root.resizeable
myroot.resizable(0,0)   # window size is fixed (cannot be larger/smaller)

mystr = StringVar() # S1
print(type(mystr))  # S2
my_entry = Entry(myroot, font = ('Cambria, 13'), textvariable = mystr)
my_entry.pack()

def myshow():
    mydata = mystr.get() #S3
    print(mydata)
    mystr.set('') # S4
    
my_btn = Button(myroot, font = ('Cambria', 13), text= 'Get Data', command= myshow)
my_btn.pack()

myroot.mainloop()


# BooleanVar()
from tkinter import *

myroot = Tk()
myroot.geometry('300x200')

num1 = BooleanVar()
mystr = StringVar()

def mydatainsertion():
    if num1.get() == True:
        mystr.set('It is set to True')
    else:
        mystr.set('It is set to False')
        
myc1 = Checkbutton(myroot, variable= num1, font = ('Cambria', 13), text= 'DREAMO', command= mydatainsertion)
myc1.pack()

mye1 = Entry(myroot, width= 20, textvariable= mystr)
mye1.pack()

myroot.mainloop() 


# IntVar()
from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0)

myint = IntVar()
myint1 = IntVar()
myint2 = IntVar()

my_entry = Entry(myroot, font = ('Cambria', 13), textvariable= myint)
my_entry.pack()

my_entry1 = Entry(myroot, font = ('Cambria', 13), textvariable= myint1)
my_entry1.pack()


def mydisplay():
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 * mydata2
    myint2.set(mydata3)
    
my_btn = Button(myroot, font = ('Cambria', 13, 'bold',), text= 'Multiply', command= mydisplay)
my_btn.pack()
my_entry2 = Entry(myroot, font= ('Cambria', 12), textvariable= myint2)
my_entry2.pack()
my_entry2.configure(state = 'readonly')

myroot.mainloop()


# DoubleVar()
from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0)

myint = DoubleVar()
myint1 = DoubleVar()
myint2 = DoubleVar()

my_entry = Entry(myroot, font= ('Cambria', 13,'bold',), textvariable= myint)
my_entry.pack()

my_entry1 = Entry(myroot, font= ('Cambria', 13, 'bold',), textvariable=myint1)
my_entry1.pack()


def mydisplay():
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 - mydata2
    myint2.set(mydata3)
    
my_btn = Button(myroot, font= ('Cambria', 13, 'bold',), text= 'Difference', command= mydisplay)
my_btn.pack()

my_entry2 = Entry(myroot, font= ('Cambria', 13), textvariable= myint2)
my_entry2.pack()
my_entry2.configure(state= 'readonly')

myroot.mainloop()


# GUI Creation Using Classes And Objects
from tkinter import *
from tkinter import messagebox
myroot = Tk()

def mydisplay():
    messagebox.showinfo('Message', 'Hey Kofi!')
    
mybtn = Button(myroot, text= 'Display', font= ('Cambria', 13, 'bold',), command= mydisplay)
mybtn.pack(padx= 20, pady= 30)
myroot.mainloop()

# Using OOP techniques to address more widgets integration
from tkinter import *
from tkinter import messagebox

class MyBtn(Tk):
    def __init__(self): # constructor
        super().__init__() # for calling the constructor of superclass
        self.mybtn = Button(self, text= 'Display', command= self.mydisplay)
        self.mybtn.pack(padx= 20, pady= 30)
        
    def mydisplay(self):
        messagebox.showinfo('Message', 'Hey Kofi!')
        
if __name__ == '__main__':
    myroot = MyBtn() # making an object of MyBtn class
    myroot.mainloop()