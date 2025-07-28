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