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