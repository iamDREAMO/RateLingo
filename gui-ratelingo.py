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
from tkinter import * # type: ignore
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
from tkinter import * # type: ignore

myroot = Tk()   # Creating blank tkinter widow
myroot.geometry('300x150')

mybtn = Button(myroot, text= 'OWUSU')
mybtn.pack(side= TOP, padx = 5, pady = 5)
myroot.mainloop()

# Changing the position of the window
from tkinter import * # type: ignore

myroot = Tk()   # Creating blank tkinter widow
myroot.geometry('300x150+400+400')

mybtn = Button(myroot, text= 'OWUSU')
mybtn.pack(side= TOP, padx = 5, pady = 5)
myroot.mainloop()


# Inbuilt Variable Classes

# SringVar()
from tkinter import * # type: ignore
myroot = Tk()   # creating an oblject of Tk class -- object of window

myroot.geometry('200x200') # window can be resized to any size until we use root.resizeable
myroot.resizable(0,0)   # type: ignore # window size is fixed (cannot be larger/smaller)

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
from tkinter import * # type: ignore

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
from tkinter import * # type: ignore
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0) # type: ignore

myint = IntVar()
myint1 = IntVar()
myint2 = IntVar()

my_entry = Entry(myroot, font = ('Cambria', 13), textvariable= myint)
my_entry.pack()

my_entry1 = Entry(myroot, font = ('Cambria', 13), textvariable= myint1)
my_entry1.pack()


def mydisplay(): # type: ignore
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 * mydata2
    myint2.set(mydata3) # type: ignore
    
my_btn = Button(myroot, font = ('Cambria', 13, 'bold',), text= 'Multiply', command= mydisplay)
my_btn.pack()
my_entry2 = Entry(myroot, font= ('Cambria', 12), textvariable= myint2)
my_entry2.pack()
my_entry2.configure(state = 'readonly')

myroot.mainloop()


# DoubleVar()
from tkinter import * # type: ignore
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0) # type: ignore

myint = DoubleVar()
myint1 = DoubleVar()
myint2 = DoubleVar()

my_entry = Entry(myroot, font= ('Cambria', 13,'bold',), textvariable= myint)
my_entry.pack()

my_entry1 = Entry(myroot, font= ('Cambria', 13, 'bold',), textvariable=myint1)
my_entry1.pack()


def mydisplay(): # type: ignore
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 - mydata2
    myint2.set(mydata3) # type: ignore
    
my_btn = Button(myroot, font= ('Cambria', 13, 'bold',), text= 'Difference', command= mydisplay)
my_btn.pack()

my_entry2 = Entry(myroot, font= ('Cambria', 13), textvariable= myint2)
my_entry2.pack()
my_entry2.configure(state= 'readonly')

myroot.mainloop()


# GUI Creation Using Classes And Objects
from tkinter import * # type: ignore
from tkinter import messagebox
myroot = Tk()

def mydisplay():
    messagebox.showinfo('Message', 'Hey Kofi!')
    
mybtn = Button(myroot, text= 'Display', font= ('Cambria', 13, 'bold',), command= mydisplay)
mybtn.pack(padx= 20, pady= 30)
myroot.mainloop()

# Using OOP techniques to address more widgets integration
from tkinter import * # type: ignore
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
    

# Getting Insights of Button Widgets in Tkinter

# tkinter Button Widget
from tkinter import * # type: ignore
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
    

# Image and State- button insights
from tkinter import * # type: ignore

class MyBtnImage(Frame):
    def __init__(self, root = None):
        Frame.__init__(self, root)
        self.root = root
        self.myphoto = PhotoImage(file = 'Add-icon.png')
        def myclick():
            self.mybtn1['state'] = DISABLED # Button text is covered by image.
        self.mybtn1 = Button(self.root, image = self.myphoto, command= myclick)
        self.mybtn1.pack(padx = 10, pady = 10)
        
if __name__ == '__main__':
    myroot = Tk()
    myobj = MyBtnImage(myroot)
    myroot.title('Image using Button')
    myroot.geometry('300x300')
    myroot.mainloop()
    

# Displaying both button image/text
from tkinter import * # type: ignore

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
    
# Events and Bindings
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
    
# Displaying message in cmd when a button is interacted
from tkinter import *
myroot = Tk() # creating the object of the Tk Class

myroot.geometry('250x100') # resizable to any size
myroot.resizable(0,0) # fixed window size

myroot.title('Event handling through Cmd prompt')

def mydisplay():
    print('Clicked !!!')
    
mytk_button1 = Button(myroot, text= 'Login', font = ('Cambri', 15, 'bold'), fg='Magenta', command= mydisplay)
mytk_button1.pack()
myroot.mainloop()

# Event handling through config() method
from tkinter import *

myroot = Tk() # creating an object of the Tk class -- object window
myroot.geometry('300x200')
myroot.resizable(0,0)

def myshow1():
    myroot.configure(background= 'Black')
    
mytk_button1 = Button(myroot, text= 'Backgorund colour change', font=('Cambria', 15, 'bold'), fg ='Cyan')
mytk_button1.config(command=myshow1)
mytk_button1.pack()

myroot.mainloop()

# Event handling using the "bind" method
from tkinter import *
myroot = Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

def myshow1(e):
    myroot.configure(background= 'LightBlue')
    
def myshow2(e):
    myroot.configure(background='LightGreen')
    
def myshow3(e):
    myroot.configure(background= 'LightYellow')
    
mytk_btn1 = Button(myroot, text = 'Background color', font=('Cambria', 14, 'bold'), fg= 'Pink')

mytk_btn1.bind('<Button-1>', myshow1)  # Left key of mouse
mytk_btn1.bind('<Button-2>', myshow2)  # Wheel Key of mouse
mytk_btn1.bind('<Button-3>', myshow3)  # Right Key of mouse
mytk_btn1.pack()

myroot.mainloop()


# Event Handling using the Lambda expression
from tkinter import *
myroot =Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

# using lambda expression
myshow1 = lambda e: myroot.configure(background= 'Cyan')
myshow2 = lambda e: myroot.configure(background='Blue')
myshow3 = lambda e: myroot.configure(background= 'LightGreen')

mytk_btn1 = Button(myroot, text='Background Colour', font=('Cambria', 14, 'bold'), fg='Brown')
mytk_btn1.bind('<Button-1>', myshow1) # left key of mouse
mytk_btn1.bind('<Button-2>', myshow2) # wheel key mouse
mytk_btn1.bind('<Button-3>', myshow3) # right key of mouse
mytk_btn1.pack()

myroot.mainloop()


# Event handling using Alphabet Keys
from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0)

myroot.bind('<Key-a>', lambda e: myroot.configure(background='LightBlue')) # on pressing key 'a'
myroot.bind('<Key-b>', lambda e: myroot.configure(background='LightGreen')) # on pressing key 'b'
myroot.bind('<Key-c>', lambda e: myroot.configure(background='Pink')) # on pressing key 'c'

myroot.mainloop()


# Event handling using single function
from tkinter import *
myroot = Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

num = 1
def mydisplay(e):
    global num
    num = num + 1
    if num%2 == 0:
        myroot.configure(background='LightBlue')
    else:
        myroot.configure(background='Brown')
        
mybtn1 = Button(myroot, text= 'Click Here!!!', font=('Cambria', 15, 'bold'))
mybtn1.bind('<Button>', mydisplay) # on mouse pressing button
mybtn1.bind('<ButtonRelease>', mydisplay) # on mouse releasing button
mybtn1.pack()

myroot.mainloop()


# tkinter Checkbutton Widget
from tkinter import *
from tkinter.ttk import *

myroot =Tk()
myroot.geometry('200x200')
myroot.title('CheckButton Widget')

def myget():
    if i2.get() == 'Check':
        s1.set('Checked')
    else:
        s1.set('Unchecked')
        
i2 = StringVar()
myc2 = Checkbutton(myroot, text= 'Check/Uncheck', variable = i2, offvalue= 'Uncheck', onvalue= 'Check', command= myget)
myc2.pack()

s1 = StringVar()
mye1 = Entry(myroot, font= ('Cambria', 14, 'bold'), textvariable= s1)
mye1.pack(pady=10)

myroot.mainloop()

# adding the selectcolor option to Checkbutton
from tkinter import *
myroot= Tk()
def selectcolor_indicatoronTrue():
    mychk1['selectcolor'] = 'Green'
    
def selectcolor_indicatoronFalse():
    mychk2['selectcolor'] = 'Yellow'
    
mychk1 = Checkbutton(myroot, text= 'CheckButton', command=selectcolor_indicatoronTrue, indicatoron=True)
mychk1.place(x=50, y=50)
mychk2 = Checkbutton(myroot, text= 'CheckButton', command=selectcolor_indicatoronFalse, indicatoron=False)
mychk2.place(x=50, y=100)
myroot.mainloop()

# adding image to the Checkbutton and the widget
from tkinter import *
myroot =Tk()

myon_image = PhotoImage(width=50, height=25)
myoff_image = PhotoImage(width=50, height=25)
myon_image.put('LightGreen', to=(0, 0,24, 24)) # put row formatted colors to image starting from position TO
myoff_image.put(('Red',), to=(25, 0 , 49, 24))

myval1 = IntVar(value=0)
myval2 = IntVar(value=1)
cb1 = Checkbutton(myroot, image= myoff_image, selectimage=myon_image, indicatoron=False, onvalue=1, offvalue=0, variable=myval1)
cb2 = Checkbutton(myroot, image=myoff_image, selectimage=myon_image, indicatoron=False, onvalue=1, offvalue=0, variable=myval2)
cb1.pack(padx=10, pady=10)
cb2.pack(padx=10, pady=10)

myroot.mainloop()


# setting the 'state' of the widget
from tkinter import *
myroot =Tk()
myroot.geometry('200x200')
def myselected():
    mychk1.config(state = NORMAL)
    
def mydisabled():
    mychk1.config(state = DISABLED)
    
mybtn1 = Button(myroot, text= 'Normal', command=myselected)
mybtn1.place(x=50, y=50)
mybtn2 = Button(myroot, text= 'Disabled', command=mydisabled)
mybtn2.place(x= 50, y= 100)

mychk1 = Checkbutton(myroot, text = 'Checkbutton')
mychk1.place(x=100, y=150)

myroot.mainloop() 


# maximum Checkbutton usage
from tkinter import *
myroot =Tk()
myroot.geometry('350x250')
myroot.title('Checkbutton Widget')

mynum1 = IntVar()
mynum2 = IntVar()
mys1 = StringVar()

def mydatainsertion():
    if mynum1.get() == 1 and mynum2.get() == 0: # read status of checkbutton
        mys1.set('DREAMO') # setting the value to  the  Entry widget
        
    if mynum1.get() == 0 and mynum2.get() == 1:
        mys1.set('Ben.COM')
        
    if mynum1.get() == 1 and mynum2.get() == 1:
        mys1.set('I am there no matter what!')
        
    if mynum1.get() == 0 and mynum2.get() == 0:
        mys1.set('I want to see both')
        
myc1 = Checkbutton(myroot, variable= mynum1, font = ('Cambria', 14, 'bold'), text='DREAMO', command=mydatainsertion)
myc1.pack()

myc2 = Checkbutton(myroot, variable= mynum2, font=('Cambria', 14, 'bold'), text='Ben.COM', command=mydatainsertion)
myc2.pack()

mye1 = Entry(myroot, font= ('Cambria', 14), textvariable=mys1)
mye1.pack()

myroot.mainloop()


# tkinter Radiobutton Widget
from tkinter import *
myroot = Tk()
myroot.geometry('200x200')

COLOR1 = 'Cyan'
COLOR2 = 'Magenta'

def mydisplay():
    if myi1.get() == 1:
        myroot.configure(bg= COLOR1)
    elif myi1.get() == 2:
        myroot.configure(bg = COLOR2)
        
myi1 =IntVar()
myr1 = Radiobutton(myroot, text = COLOR1, value= 1, variable=myi1)
myr1.pack()

myr2 = Radiobutton(myroot, text= COLOR2, value= 2, variable=myi1)
myr2.pack()

mybtn = Button(myroot, text= 'Background_Click', command=mydisplay)
mybtn.pack()

myroot.mainloop()


# display image to a radiobutton
from tkinter import *
myroot = Tk()

myon_image = PhotoImage(width=50, height=25)
myoff_image = PhotoImage(width=50, height=25)
myon_image.put(('Brown'), to=(0, 0 , 24, 24)) # put row formatted colors to image starting from position TO
myoff_image.put(('Red',), to=(0,0,24,24))

myrbvar = IntVar(value=1)
myrb1 = Radiobutton(myroot, variable=myrbvar, value=0, bd=0, text='RadioButton1', compound='left', indicatoron=False, image=myoff_image, selectimage=myon_image)
myrb2 = Radiobutton(myroot, variable=myrbvar, value=1, bd=0, text='Radiobutton2', compound='left', indicatoron=False, image=myoff_image, selectimage=myon_image)
myrb1.pack(padx=10, pady=10)
myrb2.pack(padx=10, pady=10)

myroot.mainloop()

# Radiobutton with text
from tkinter import *
myroot = Tk()

myrb1 = Radiobutton(myroot, value=0, text='Radiobutton1', bg= 'lightGreen', indicatoron=False)
myrb2 = Radiobutton(myroot, value=1, text='RadioButton2', bg = 'lightGreen', indicatoron=False)
myrb1.pack(padx=10,pady=10)
myrb2.pack(padx=10,pady=10)

myroot.mainloop()


# tkinter OptionMenu Widget
from tkinter import *
myroot = Tk()
myroot.title('Car Selection')
myroot.geometry('300x300')

myvar = StringVar() # tk variable created
myvar.set('Cars')

# create an option menu by passing the variable and option list
myselection = OptionMenu(myroot, myvar, 'BMW', 'Benz', 'Ford', 'Kia', 'Toyota') # variable bound to option menu
myselection.pack()

# create button with command
def mydisplay():
    print('The chosen car :', myvar.get())
    
mybtn = Button(myroot, text= 'My Choice',command=mydisplay)
mybtn.pack(pady=30, side= BOTTOM, anchor= N)

myroot.mainloop()


# Insight of the Input Widget in tkinter
# tkinter Entry Widget
from tkinter import *

class MySTATE:
    def __init__(self, myroot):
        self.myvar = StringVar()
        self.myvar.set('Benedict')
        
        self.myl1 = Label(myroot, text= 'Normal State')
        self.myl1.grid(row=0, column=0)
        
        self.myl2 = Label(myroot, text='Disabled state')
        self.myl2.grid(row=1, column=0, pady=10)
        
        self.myl3 = Label(myroot, text= 'Readonly state')
        self.myl3.grid(row=2, column=0, pady=10)
        
        self.mye1 = Entry(myroot, textvariable=self.myvar, width=15, state='normal')
        self.mye1.grid(row=0, column=1, padx=10)
        
        self.mye2 = Entry(myroot, textvariable=self.myvar, width=15, state='disabled')
        self.mye2.grid(row=1, column=1, padx=10)
        
        self.mye3 = Entry(myroot, textvariable=self.myvar, width=15, state= 'readonly')
        self.mye3.grid(row=2, column=1, padx=10)
        
if __name__ == '__main__':
    myroot = Tk()
    myobj = MySTATE(myroot)
    myroot.mainloop()


# 'show' and 'selectborderwidth' option with Entry()
from tkinter import *

class MyLogin:
    def __init__(self, myroot):
        self.myl1 = Label(myroot, text= 'Username')
        self.myl1.grid(row=0, column=0)
        
        self.myl2 = Label(myroot, text='Password')
        self.myl2.grid(row=1, column=0, pady=10)
        
        self.mye1 = Entry(myroot, width=15, selectborderwidth = 3)
        self.mye1.grid(row=0,column=1,padx=10)
        
        self.mye2 = Entry(myroot, width=15, show='*')
        self.mye2.grid(row=1, column=1, padx=10)
        
        def mydisplay():
            print('The username is: ' + self.mye1.get())
            print('The password is: ' + self.mye2.get())
            
        self.mybtn = Button(myroot, text= 'Login', command=mydisplay, font= ('Cambria', 12, 'bold'))
        self.mybtn.grid(row=2, columnspan= 3)
        
if __name__ == '__main__':
    myroot = Tk()
    myobj = MyLogin(myroot)
    myroot.title('Login Page')
    myroot.geometry('200x150')
    myroot.mainloop()


# delete( first, last=Name ) with Entry widget
from tkinter import *

class MydeleteEg(Tk):
    def __init__(self):
        super().__init__()
        self.title('MyDelete Eg')
        self.mye1 = Entry(self, font = ('Cambria', 14, 'bold'), width= 30, bd = 5)
        self.mye1.pack(side=LEFT)
        
        self.btn1 = Button(self, text='Delete the text', command= lambda: mydelete(self, self.mye1))
        self.btn1.pack(pady=32)
        
        def mydelete(self, myentry):
            myentry.delete(first=0, last=15)
            
if __name__ == '__main__':
    myroot = MydeleteEg()
    myroot.geometry('500x100')
    myroot.mainloop()
    

# get(), icusor(), insert() options for Entry widget
from tkinter import *

class MyCursorPosition(Tk):
    def __init__(self):
        super().__init__()
        self.title('MyCursorPosition Eg.')
        self.mye1 = Entry(self, font=('Cambria', 13, 'bold'), width=20, bd=5)
        self.mye1.pack(side=LEFT)
        self.mye1.focus()
        self.mye1.insert(0, 'Demonstration')
        self.mye1.icursor(0)
        
        self.btn = Button(self, text= 'Position the cursor', command=lambda: myposition(self, self.mye1))
        self.btn.pack(pady= 32)
        
        def myposition(self, myentry):
            myentry.icursor(5)
            
if __name__ == '__main__':
    myroot = MyCursorPosition()
    myroot.geometry('500x100')
    myroot.mainloop()
    

# index(index), select_adjust()
from tkinter import * 

class MyIndex_Select_adjust(Tk):
    def __init__(self):
        super().__init__()
        self.title('MyIndex and Select_adjust Eg.')
        self.mye1 = Entry(self, font=('Cambria', 14, 'bold'), width=20, bd=5)
        self.mye1.pack(side=LEFT)
        self.mye1.focus()
        self.mye1.insert(0, 'Demonstration')
        self.mye1.icursor(0)
        
        self.btn = Button(self, text='Index', command=lambda: myindex(self, self.mye1))
        self.btn.pack(pady=10)
        
        self.btn1 = Button(self, text='select_adjust', command=lambda: myselect_adjust(self, self.mye1))
        self.btn1.pack(pady=10)
        
        def myindex(self, myentry):
            myentry.icursor(self.mye1.index(6))
            
        def myselect_adjust(self, myentry):
            myentry.select_adjust(5)
            
if __name__ == '__main__':
    myroot = MyIndex_Select_adjust()
    myroot.geometry('500x100')
    myroot.mainloop()
    
    
# xview_scroll, xview
from tkinter import *

class MyScrollbarEntry(Tk):
    def __init__(self):
        super().__init__()
        mysobj_scroll = Scrollbar(self, orient='horizontal')
        mye1 = Entry(self, xscrollcommand= mysobj_scroll.set, font=('Helvectica',13, 'bold'))
        mye1.focus()
        mye1.pack(side='bottom', fill=X)
        mysobj_scroll.pack(fill=X)
        mysobj_scroll.config(command=mye1.xview)
        mye1.insert(0, 'You are the only one who can stop your dreams. Be very OPTIMISTIC about your dreams and pursue them with purpose!')
        
if __name__ == '__main__':
    myroot = MyScrollbarEntry() 
    myroot.geometry('500x200') 
    myroot.mainloop() 
    

# Validation in Entry Widget
from tkinter import *
class MyValidate(Tk):
    def __init__(self):
        super().__init__()
        self.my10 = Label(self, text='Enter the number:', fg='Magenta', font =('Cambria', 12, 'bold'))
        self.my10.place(x=10, y=30)
        
        self.mye1 = Entry(self, font=('Helvetica', 13))
        self.mye1.place(x=150, y=30)
        
        self.myl1 = Label(self, text='', fg='Red')
        self.myl1.place(x=70, y=50)
        
        self.myreg = self.register(self.mycallback) # v1
        self.invalidcmd = self.register(self.myinvalid_name) # v2
        self.mye1.config(validate= "key", validatecommand=(self.myreg, '%P'), invalidcommand=(self.invalidcmd, '%S')) #v3
        
    def mycallback(self, myinp):
        if myinp.isdigit(): # c1
            print(myinp)
            self.myl1.config(text='')
            return True
        
        elif myinp is "":       # c2
            print(myinp)
            self.myl1.config(text='')
            return True
        
        else: # c3
            print(myinp)
            return False
            
    def myinvalid_name(self, myCh):
        self.myl1.config(text=(f'Invalid character (myCh) \n name can only have numbers'), font= ('Arial', 11, 'bold'))
            
if __name__ == "__main__":
    myroot = MyValidate()
    myroot.geometry('400x100')
    myroot.mainloop()
    
    
# tkinter Scrollbar widget
# Scrollbar attached to Listbox
from tkinter import *
class Scrollbar_ListBox(Tk):
    def __init__(self):
        super().__init__()
        
        self.mysclbar = Scrollbar(self) # scrollbar creation and attaching to the menu window
        self.mysclbar.pack(side=RIGHT, fill='y') # scrollbar added to the window right side 
        
        self.mylstbox = Listbox(self) # listbox creation and attaching to the main window
        self.mylstbox.config(yscrollcommand=self.mysclbar.set) # scrollbar attached to the listbox for vertical scroll used yscrollcommand
        
        for loop in range(50): # insertelements from 0 to 49 in the listbox
            self.mylstbox.insert(END, str(loop))
            
        self.mylstbox.pack(side='left', fill=BOTH) # listbox added to the window left side
        self.mysclbar.config(command=self.mylstbox.yview) # for need of vertical view settings scrollbar command option to listbox.yview method
        
if __name__ == '__main__':
    root = Scrollbar_ListBox()
    root.mainloop()

# Scrollbar attached to Text
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


# Scrollbar attached to Canvas            
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
    

# Scrollbar attached to Entry
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
    
    
# tkinter Spinbox widget
from tkinter import *

root = Tk()
root.geometry('200x200')
root.title('SpinBox')

# spinbox creation
spin = Spinbox(font=('Cambria', 14, 'bold'), from_=10, to=20)
spin.pack()
root.mainloop()


# specify set of values in spinbox
from tkinter import *
root = Tk()
root.geometry('200x200')
root.title('SpinBox Values Specified')

# creation of spinbox
spin1 = Spinbox(font= ('Cambria', 14, 'bold'), values=(10,15,20,25,30), bd=10, relief= RIDGE)
spin1.pack()
root.mainloop()

# display str values with spinbox
from tkinter import *
root = Tk()
root.geometry('300x300')

# StringVar Variable
stv = StringVar()

# display function
def display():
    root.configure(bg= stv.get())
    
# creation of spinbox
spin = Spinbox(font= ('Cambria', 14, 'bold'), command=display,
               values= ['Red', 'Green', 'Blue', 'Pink', 
                        'Magenta', 'Yellow'], textvariable=stv)
spin.pack()
root.mainloop()

# disable clicking in spinbox
from tkinter import * 
root = Tk()
root.geometry('350x200')
root.title('SpinBox with Disabled Clicking')

# spinbox creation
spin1 = Spinbox(font= ('Cambria', 14, 'bold'), values=(10,35,49,50,60,23), state='readonly')
spin1.pack(pady=10)
root.mainloop()


# tkinter Scale Widget
from tkinter import * 
root = Tk()

# creating a float variable value holder
var1 = DoubleVar()

# creating horizontal slider
h_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, 
                 length= 200, width=10, sliderlength=50, label='myscale',
                 variable=var1)

# set the scale value to 45
h_slider.set(45)
h_slider.pack()

def display():
    # will get the value
    print(var1.get())
    # will return the coordinates corresponding to the given scale value
    print(h_slider.coords(value=var1.get()))
    
# creating a button widget
btn = Button(root, text='GetValue', command=display, bg='LightBlue')
btn.pack(pady=10)

root.title('Scale_Widget')
root.geometry('300x200+120+120')
root.mainloop()
    

# tkinter Text Widget
from tkinter import *
root = Tk()
root.geometry()
root.title('Text Widget')

#creating the text widget
text1 = Text(root, width=18, height=10, font=('Cambria', 12, 'bold'), wrap =WORD, 
             padx=10, pady=10, bd=4, selectbackground='Grey', selectforeground='Black')
text1.pack()
root.mainloop()

# Read entire contents in Text Widget
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x300')
root.title('Text_Widget Content')

# Text widget creation
txt = Text(root, width=18, height=12, 
           font=('Arial', 12), wrap = WORD,
           padx=10, pady=10, bd=4, 
           selectbackground='Grey', selectforeground='Blue')
txt.pack()

# inserting text in the text widget
txt.insert('1.0', 'Beginner! Welcome to learning tkinter text widget. \n This is for multiple lines.')

# callback function
def myget():
    messagebox.showinfo('Text widget contents are: ',
                        txt.get('1.0', 'end')) # reading the entire content displaying
    
btn = Button(root, text='Read', command=myget)
btn.pack()
root.mainloop() 


# Add a tag to the Text Widget
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Tag to Text_Wigdet')

text = Text(root, width=18, height=10, font=('Cambria', 14, 'bold'), wrap=WORD, padx=10,
            pady=10, bd=4, selectbackground='Blue', selectforeground='Green')
text.pack()

text.insert('1.0', 'This is the First line')
text.insert('1.0 + 1 line', '\nThis is Second Line')
text.insert('1.0 + 2 lines', '\nThis is the Third Line')

# 1st par: Name of the tag which  will be created as a string
# 2nd par: start
# 3rd pas: end
text.tag_add('Tag', '1.0', '1.0 wordend')

# Confir=guring the properties about the tag
text.tag_configure('Tag', background='Brown')
root.mainloop()


# Getting Marks in the Text Widget
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Mark in Text_Widget')

# text widget
text = Text(root, width=18, height=10, font=('Cambria', 12), wrap=WORD, 
            padx=10, pady=10, bd=4, selectbackground= 'LightBlue', 
            selectforeground= 'White')
text.pack()

text.insert('1.0', 'This is the first line')
text.insert('1.0 + 1 line', '\nThis is the second line' )
text.insert('1.0 + 2 lines', '\nThis is the third line')

print(text.mark_names())
root.mainloop()


# Inserting Image in Text widget
from tkinter import *
root = Tk()

def click():
    text1.insert('insert',"<>")
    
btn = Button(root, text='Click Here!', command=click)
btn.pack()

text1 = Text(root, width=55, height=30)
text1.pack()

def insertimage():
    text1.image_create('insert', image = image1)

image1 = PhotoImage(file='Add-icon.png')
btn1 = Button(root, text='CreateImage', command=insertimage)
btn1.pack(pady=10)
root.mainloop()


# Tkinter Combobox Widget
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('300x200')
root.title('Combobox Widget')

# List of values
List1 = list(range(1,10))

combo = Combobox(root, values=List1, width=15)
combo.pack(padx=40, pady=10) 
root.mainloop()