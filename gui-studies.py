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


# Add string list as values in Combobox
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('350x200')
root.title('Combobox with String as Values')

# string values
str_v = ['Translation', 'Transcription', 'Voice Over', 'Subtitling']

combo1 = Combobox(root, values= str_v, height=2)
combo1.pack()

root.mainloop()

# Displaying text in the combobox
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('300x200')
root.title('Text in Combobox')

str_val = StringVar()

def display():
    str_val = combo.get()
    print(str_val)
    
list1 = ['Ghana','Togo','Algeria','Morocco']
str_val.set('Ghana')

combo = Combobox(root, values= list1, height=5, textvariable=str_val, postcommand=display)
combo.pack()

root.mainloop()


# Assigning font to combobox
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('350x300')
root.title('Specified Font in Combobox') 

# list of values
list2 = ['Translation', 'Transcription', 'Subtitling','Voice Dubbing']

# assigning font
font1 = ('Cambria', 12, 'bold', 'italic')

# assigning label
lab1 = Label(root, text = 'Choose the service', font=('Cambria', 12, 'bold'))
lab1.pack(pady=5)

# combobox object
combo = Combobox(root, values= list2, height=5, font= font1)
combo.pack(pady= 2)
combo.current(1)

# specify font of the box of combobox
root.option_add('*TCombobox*Listbox.font', font1)
root.mainloop()


# Getting Insights of Display Widgets in tkinter
from tkinter import *
root = Tk()

root.maxsize(300,300) # maximum size of the window set up to 300 only
root.resizable(0,0) # fixed window size

label1 = Label(root, text= 'Tkinter\nis\nAwesome', font=('Cambria', 18, 'bold'),
               bg= 'Cyan', fg= 'Black', width= '16', height= '4')
label1.pack()
root.mainloop()


# Positioning text in Label Widget
from tkinter import *

class LabelPosition(Tk):
    def __init__(self):
        super().__init__()
        self.title('Position Text within a Label')
        self.label1 = Label(self, text = 'Hello! \n Welcome!', bd=4, relief = SUNKEN, 
                           font= 'Hevectica 14', width=10, height=4, anchor= SW)
        self.label1.pack()
        
if __name__ == '__main__':
    root = LabelPosition()
    root.mainloop()


# Justify text in Label
from tkinter import *

class Just1(Tk):
    def __init__(self):
        super().__init__()
        self.title('Justify the Label')
        lab1 = Label(self, text= 'KOFI')
        lab1.pack()
        lab2 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12))
        
        # default justify is CENTER
        lab2.pack()
        lab3 = Label(self, text= 'KOFI')
        lab3.pack()
        lab4 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12), justify = LEFT)
        lab4.pack()
        lab5 = Label(self, text= 'Hello\nThere There\nThere There There', 
                     bd=2, relief= 'solid', font= ('Cambria',12), justify = RIGHT)
        lab5.pack()
        
if __name__ == '__main__':
    root = Just1()
    root.geometry('350x300')
    root.mainloop()
    
    
# Access the options of tkinter label
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
    

# Using textvariable options with label widget
from tkinter import *

class StrVartext(Tk):
    def __init__(self):
        super().__init__()
        self.vall = StringVar()
        self.title('StringVar/textvariable as Tk label')
        self.lab1 = Label(self, font =('Cambria', 12, 'bold'),
                          textvariable = self.vall, relief = 'groove')
        self.lab1.pack()
        self.vall.set('Tkinter is great')
        
if __name__ == '__main__':
    root = StrVartext()
    root.geometry('300x300')
    root.mainloop()
    
    
# Tkinter Message Widget
from tkinter import *
root = Tk()
Str1 = StringVar()

# Message widget object
msg1 = Message(root, textvariable= Str1, relief=SUNKEN, 
               font =('Arial', 12,'bold'),fg = 'Cyan', bg = 'Brown')
Str1.set('Display of string message')
msg1.pack()
root.geometry('200x200')
root.mainloop()

# Usinf Text option to display message
from tkinter import *
root = Tk()

text1 = 'This session is to test my knowledgr so far with tkinter'
msg1 = Message(root, text=text1, font =('Cambria', 12, 'bold'),
               fg="Blue", bg='Magenta', relief= RAISED)
msg1.pack()
root.geometry('200x200')
root.mainloop()
    
    
# Statusbar in Tkinter
from tkinter import *

root = Tk()
root.geometry('200x150')
root.title('StatusBar_Example')

statusbar = Label(root, text='Example of StatusBar...', 
                  bd=1, relief=GROOVE, anchor=W) # for text aliginment within label

statusbar.pack(side=BOTTOM, fill=X) 
root.mainloop()


# tkinter MessageBox Widget
# (displays the message boxes in the python application)

# showinfo()
# (displays the relevant info to the user)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')
root.title('Showinfo function')

def display():
    messagebox.showinfo('showinfoexample', 'Basic showinfo example')
btn1 = Button(root, text= 'Clickinfo', command = display)
btn1.pack()
root.mainloop()

# showwarning()
# (display warning message to the user)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')
root.title('Warningmessage')

def display():
    messagebox.showwarning('Showwarningexample', 'Basic warning message example')
btn1 = Button(root, text = 'ClickWarningMessage', command= display)
btn1.pack()
root.mainloop()

# showerror()
# (display error message to the user) 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')
root.title('Errormessage')

def display():
    messagebox.showerror('Showerrorexample', 'Basic error message example')
btn1= Button(root, text = 'ClickErrorMessage', command = display)
btn1.pack()
root.mainloop()

# askquestion()
# (display custom confirmatory questions to the user either Yes/No)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')
root.title('AskQuestion')

def display():
    answer = messagebox.askquestion('AskQestion example', 'Do you want to continue?')
    if answer == 'yes':
        messagebox.showinfo('Message', 'You have selected Yes')
    else:
        messagebox.showinfo('Message', 'You have selected No')
        
btn1 = Button(root, text= 'ClickAskMessage', command= display)
btn1.pack()
root.mainloop()

# askokcancel()
# (confirms the user's responses concerning the app activity)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')
root.title('AskOkCancel')

def display():
    messagebox.askokcancel('AskOkCancel example', 'Redirecting to www.abc.com')
btn1 = Button(root, text= 'ClickOkCancel', command = display)
btn1.pack()
root.mainloop()

# askyesno()
# (questions the user to provide Yes/No answer)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x300')
root.title('AskYesNo')

def display():
    messagebox.askyesno('AskYesNo example', 'Do you want to continue the process?')
btn1 = Button(root, text= 'ClickYesNoMessage', command= display)
btn1.pack()
root.mainloop()

# askretrycancel
# (ask user perform task again or not)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x300')
root.title('AskRetryCancel')

def display():
    messagebox.askretrycancel('AskRetryCancel example', 'Was the process successful?')
btn1= Button(root, text= 'ClickRetryCancelMessage', command= display)
btn1.pack()
root.mainloop()


# Insights of Container Widgets in tkinter
# (ability to manage and organise the layout widgets in the GUI)

# tkinter Frame Widget
# (responsible for arrangement of widget positions)

from tkinter import *

root = Tk()
root.geometry('300x300')

frame1=Frame(root, width=150,height=150, bg='Red')
frame1.grid(row=0, column=0)

frame2=Frame(root, width=150,height=150, bg='Green')
frame2.grid(row=1, column=0)

frame3=Frame(root, width=150,height=150, bg='Blue')
frame3.grid(row=0, column=1)

frame4=Frame(root, width=150,height=150, bg='Cyan')
frame4.grid(row=1, column=1)

root.mainloop()


# Add input to the frame
from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('Frame Input')

frame1=Frame(root)
l1= Label(frame1, text = 'Name')
l1.grid(row=0, column=0)
l2= Label(frame1, text = 'Age')
l2.grid(row=1, column=0)
l3= Label(frame1, text = 'Contact')
l3.grid(row=2, column=0)

ent1 = Entry(frame1)
ent1.grid(row=0, column=1)
ent2 = Entry(frame1)
ent2.grid(row=1, column=1)
ent3 = Entry(frame1)
ent3.grid(row=2, column=1)

btn = Button(frame1, text= 'View')
btn.grid(row=3, columnspan= 2)
frame1.grid(row=3, column=0)

root.mainloop()


# tkinter LabelFrame Widget
# (acts as a container to group interrelated widgets with borders)

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
    
    
# tkinter Tabbed/Notebook Widget
# (tabbed widgets are created using the ttk module)

from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('Tab Widget Demo')
tabcontrol = ttk.Notebook(root) # L1

tab1 = ttk.Frame(tabcontrol) #L2
tab2 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1, text = 'Tab-1') # L3
tabcontrol.add(tab2, text = 'Tab-2')
tabcontrol.pack(expand = 1, fill = 'both') # L4

ttk.Label(tab1, text = 'This is Tab1', 
font= ('Helvetica', 12, 'bold')).grid(column=0, row=0, padx= 50, pady=50) # L5
ttk.Label(tab2, text = 'This explains the how tabs work in tkinter', 
font= ('Calibri', 12, 'bold')).grid(column=0, row=0, padx= 50, pady=50)

root.mainloop()


# tkinter PanedWindow Widget
from tkinter import *
root =Tk()
root.geometry('300x300')

# first paned window object
pw = PanedWindow(root)
pw.pack(fill=BOTH, expand= 1)

ent = Entry(pw, bd=5, relief='groove', font =('Arial', 12), bg='LightGreen')
pw.add(ent)

# second paned window widget
pw1 = PanedWindow(pw, orient=VERTICAL)
pw.add(pw1) # add second paned window to first paned window

ent1 = Spinbox(pw1, from_=10, to= 20, font =('Helvetica', 12), bg='LightBlue')
pw.add(ent)

ent2 = Entry(pw1, bg ='brown', relief='sunken',font =('Arial', 12))
ent2.insert(0,3) # set value to 3

pw.configure(sashrelief= RAISED) # show sash

# subtraction function
def subtract():
    num1 = int(ent1.get()) # get value of spinbox
    num2 = int(ent2.get()) # get value of entry
    data1 = str(num1-num2)
    ent.insert(1, data1)
    
# add spinbox to second paned window
pw1.add(ent1)

# add entry to second paned window
pw1.add(ent2)

# create button widget
btn = Button(pw1, text='Subtract', command=subtract)

# add button to second paned window
pw1.add(btn)

root.mainloop()


# tkinter Toplevel Widget
# (acts as Frame; contained in a window and will create/display the toplevel windows)

from tkinter import *
root = Tk()
root.geometry('250x250')

def navigate():
    # top level object for creation of a new window
    topobj = Toplevel(root)
    topobj.geometry('250x250')
    # getting the title for the window
    topobj.title('New_Window')
    # infinitely running mainloop
    topobj.mainloop()
    
# button object for opening new window
btn = Button(root, text='Navigate', command=navigate)
# position the button
btn.place(x=100, y=100)
root.mainloop()

# control the stacked nature of each windows
from tkinter import *

# create main window
root = Tk()
root.geometry('300x300')
root.title('Main Window')
topobj = Toplevel(root)

# create new window
topobj.title('New Window')
topobj.geometry('300x300')
root.lift(topobj)

root.mainloop()

# control the state/visibility of the windows
# (state: normal, iconic, withdrawn)
from tkinter import *

# create main window
root = Tk()
root.geometry('300x300')
root.title('Main Window')
topobj = Toplevel(root)

# create new window
topobj.title('New Window')
topobj.geometry('300x300')
topobj.lift(root)
topobj.state('iconic')

root.mainloop()


# Insights of Item Widgets in tkinter
# (user gets to  select items from a list display using the Listbox)
from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('A ListBox')

def myget():
    linenumber = lb1.curselection() # get the line number
    for loop in linenumber:
        print(loop, ':', lb1.get(loop)) # get item of that line number
        
# create ListBox with specified width and height
lb1 = Listbox(root, width= 30, height= 15, 
                bg='Cyan', font=('Arial', 12, 'bold'), selectmode = BROWSE)

# insert one or more lines into ListBox
lb1.insert(1, 'Translation')
lb1.insert(2, 'Subtitling')
lb1.insert(3, 'Transcription')
lb1.pack()    # corrected the error in the code in the book for fig 7.1

mybtn = Button(root, text='Line number display', 
               font=('Arial', 12, 'bold'), command=myget)
mybtn.pack()

root.mainloop()


# Insights of Interactive Widgets in tkinter
# (users have the ability to design intuitive GUIs)
# tkinter Menu Widget
# (a top-level menu displayed under the parent window's title bar)
from tkinter import *

root = Tk()
def greet():      # called when Welcome! menu item is clicked
    print('Akwaaba!')
    
menu = Menu(root) # create a toplevel menu
menu.add_command(label = 'Akwaaba!', command=greet) # add menu items to main menu
menu.add_command(label = 'Quit!', command =root.quit) # will close GUI
root.config(menu = menu) # display of menu

root.mainloop()

# change the label of an item in the menu using entryconfig()
from tkinter import *
root = Tk()
menu_bar = Menu(root)

def selected(menu):
    menu.entryconfig(1, label= "Selected!")
    
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label= "Demo1", command=lambda: selected(edit_menu))

menu_bar.add_cascade(label= "Edit", menu=edit_menu)
root.config(menu=menu_bar)

root.mainloop()


# tkinter Menubutton Widget
# (a drop-down menu part shown to the user to make choices)
from tkinter import *
root = Tk()
root.geometry('350x350')
root.title('MenuButton Widget')

# create menu button with speicied options
game_list = Menubutton(root, text= 'Games', font=('Cambria', 12, 'bold'),
                       justify=CENTER, relief='groove')

# create the drop down menu to be visible when clicked
games = Menu(game_list)
game_list.config(menu=games)

# add commands to the drop down menu
games.add_command(label='Ampe')
games.add_command(label='Mirikatuo')
games.add_command(label='Antoakyire')
game_list.pack()

root.mainloop()