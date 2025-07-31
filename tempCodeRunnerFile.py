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