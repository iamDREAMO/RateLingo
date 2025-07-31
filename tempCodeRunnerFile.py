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
lab1.pack(pady=2)

# combobox object
combo = Combobox(root, values= list2, height=5, font= font1)
combo.pack(pady= 2)
combo.current(1)

# specify font of the box of combobox
root.option_add('*TCombobox*Listbox.font', font1)
root.mainloop()