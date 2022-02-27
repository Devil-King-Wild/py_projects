import tkinter as tk

from tkinter import messagebox
import time


root = tk.Tk()
root.title('L O G I N')


logs = open('log info.txt', 'r')
info = logs.readlines()

#MAIN LOGIN HERE

def login():
    if password.get()=='123' and username.get()=='123':
        itsu = tk.Label(text = 'success', fg = 'green')
        itsu.place(x = 219, y = 190)
        print("UNLOCKED")
        time.sleep(7)
        exit()

    elif password.get()=='' and username.get()=='':
        nothing = tk.Label(text='do some thing')
        nothing.place(x=210, y=200)


    else:
        itsnot = tk.Label(text = 'wrong one', fg = 'red')
        itsnot.place(x = 210, y = 200)
        messagebox.showinfo('wrong one', 'get off')



window = tk.Canvas(root, height=280, width=480)
window.pack()

welcome = tk.Label(text = 'SIGIN IN')
welcome.place(x = 210, y = 20)

button = tk.Button(text = 'LOGIN', command = login)
button.place(x = 220, y = 230)

#username

label1 = tk.Label(text = 'username')
label1.config(font=8)
label1.place(x = 210, y = 57)

username = tk.Entry(bg = 'pink')
username.config(font=1)
username.place(x = 150, y = 80)


#password

label2 = tk.Label(text = 'password')
label2.config(font=8)
label2.place(x = 210, y = 106)

password = tk.Entry(bg = 'pink')
password.config(font=1)
password.place(x = 150, y = 130)





root.mainloop()

