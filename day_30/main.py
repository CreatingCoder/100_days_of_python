from tkinter import *
import random as rand
import json

alphabet = "!#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
password_length = 12

################# FUNCTIONS ##################




def gen_pass():
    global generated_pass
    generated_pass = ''
    for i in range(0, password_length):
        random_num = rand.randint(0,92)
        generated_pass = generated_pass + alphabet[random_num]
    E3.insert(0, generated_pass)

def add():
    global entry
    global entry2
    entry = E1.get()
    entry2 = E2.get()
    entry3 = E3.get()


    if entry !='' and entry2 != '' and entry3 != '':
        json_file = json.dumps(entry +'   |   '+ entry2 + '   |   ' + entry3)

        with open('passwords.json', 'w') as outfile:
            outfile.write(json_file)


def search():
    print('search function called')

    json_file = open('passwords.json')

    #type str
    jdata = json.load(json_file)

    if('facebook' in jdata):
        print('found facebook')


                
    #TODO: open and search json file 

##################

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
L1 = Label(window, text="Website")
L1.grid(column=3, row=2,)

E1 = Entry(window, bd =5)
E1.grid(column=4, row=2)

search = Button(text='Search', command = search)
search.grid(column=5,row=2)


L2 = Label(window, text="Email/Username")
L2.grid(column=3, row=3,)

E2 = Entry(window, bd =5)
E2.grid(column=4, row=3)


L2 = Label(window, text="Password")
L2.grid(column=3, row=4,)

E3 = Entry(window, bd =5)
E3.grid(column=4, row=4)

gen_pass = Button(text='Generate Password', command = gen_pass)
gen_pass.grid(column=4,row=5)

add = Button(text='Add', command = add)
add.grid(column=4,row=6)


window.mainloop()
