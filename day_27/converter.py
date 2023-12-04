##Converts Miles into Kms

import tkinter
from tkinter import messagebox 

window = tkinter.Tk()

window.title('Conversion App')
window.minsize(600,200)

label = tkinter.Label(text='Converter', font=("Arial", 25))

lbl = tkinter.Label(window, text = "Enter Miles: ")
lbl.grid(column =0, row =0)
 

txt = tkinter.Entry(window, width=10)
txt.grid(column =1, row =0)


def convert():
    int_txt = txt.get()
    answer = float(int_txt) * 1.60934
    msg=messagebox.showinfo("KMs", f"{answer}")


button = tkinter.Button(text = 'Convert', command = convert)
button.grid(column=2,row=2)







window.mainloop()
