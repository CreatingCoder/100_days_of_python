from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
window.geometry("500x800")


canvas = Canvas(width=300, height=300, bg='gray', highlightthickness= 0)


#Image
lock_img = PhotoImage(file="lock.gif")
canvas.create_image(150,112, image=lock_img)
canvas.grid(column=4, row=0, pady=40, padx = 15)

#
L1 = Label(window, text="User Name")
L1.grid(column=3, row=2,)


E1 = Entry(window, bd =5)
E1.grid(column=4, row=2,)







window.mainloop()
