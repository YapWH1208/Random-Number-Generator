import random
from tkinter import *

# Function
def refresh(V1, V2):
    New_V = random.randint(int(V1), int(V2))

    Number.set(New_V)

window = Tk()

# Text Variable
Min = StringVar()
Max = StringVar()
Number = StringVar()

# Label
Title_Label = Label(window, text="Random Number Generator")
Title_Label.grid(row=1, sticky=N)

Ins_Label = Label(window, text="Input the range of the number in the box")
Ins_Label.grid(row=3, sticky=N)

Min_Label = Label(window, text="Minimum")
Min_Label.grid(row=5, sticky=W)

Max_Label = Label(window, text="Maximum")
Max_Label.grid(row=6, sticky=W)

Random_Label = Label(window, textvariable=Number, font=("Arial", 20))
Random_Label.grid(row=8, sticky=S)

# Entry
Min_Entry = Entry(window, textvariable=Min)
Min_Entry.grid(row=5, sticky=E)

Max_Entry = Entry(window, textvariable=Max)
Max_Entry.grid(row=6, sticky=E)

# Button
Refresh_Button = Button(window, text="Refresh", command=lambda: refresh(Min.get(),Max.get()))
Refresh_Button.grid(row=7)

window.mainloop()





