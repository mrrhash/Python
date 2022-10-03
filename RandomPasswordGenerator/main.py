from tkinter import *
from random import randint

root = Tk()
root.title('Random Password Generator')
root.geometry("500x300")


def new_randomPassword():

    pass_entry.delete(0, END)

    pass_length = int(entry.get())

    my_password = ''

    for x in range(pass_length):
        my_password += chr(randint(33,126))

    pass_entry.insert(0, my_password)    

def copy_password():
    
    root.clipboard_clear()

    root.clipboard_append(pass_entry.get())


LF = LabelFrame(root,text="How many Characters?")
LF.pack(pady=20)

entry = Entry(LF,font=("Roboto",24))
entry.pack(pady=20,padx=20)

pass_entry = Entry(root,text='',font=("Roboto",24),bd=0,bg='systembuttonface')
pass_entry.pack(pady=20)

frame = Frame(root)
frame.pack(pady=20)

my_button = Button(frame, text="Generate Password" , command=new_randomPassword)
my_button.grid(row=0 , column=0 , padx=10)

copy_button = Button(frame , text="Copy to Clipboard" , command=copy_password)
copy_button.grid(row=0 , column=1 , padx=10 )



root.mainloop()
