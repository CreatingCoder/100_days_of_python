from tkinter import *

#################3

def gen_pass():
    print('Hello World')

def add():
    print('Add')
    global entry, entry2
    entry = E1.get()
    entry2 = E2.get()
    
    file = open('yeet.txt', 'a')
    file.write(entry + '  |  ' + entry2 + '/n')
    

    file.close()



##################

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
window.geometry("500x800")

#website_var = 


canvas = Canvas(width=300, height=300, bg='gray', highlightthickness= 0)


#Image
lock_img = PhotoImage(file="lock.gif")
canvas.create_image(150,112, image=lock_img)
canvas.grid(column=4, row=0, pady=40, padx = 15)

#
L1 = Label(window, text="Website")
L1.grid(column=3, row=2,)

E1 = Entry(window, bd =5)
E1.grid(column=4, row=2)


L2 = Label(window, text="Email/Username")
L2.grid(column=3, row=3,)

E2 = Entry(window, bd =5)
E2.grid(column=4, row=3)


L2 = Label(window, text="Password")
L2.grid(column=3, row=4,)

E2 = Entry(window, bd =5)
E2.grid(column=4, row=4)

gen_pass = Button(text='Generate Password', command = gen_pass)
gen_pass.grid(column=4,row=5)

add = Button(text='Add', command = add)
add.grid(column=4,row=6)
















window.mainloop()
