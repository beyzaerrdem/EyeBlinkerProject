import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title("Eye Blinker Login")
root.geometry("925x500")
root.config(bg="#d8b8d8")
root.resizable(False,False)  #width height değiştirme kapalı



loginLabel = Label(root, width=10,height=3, text="UserName: ",font=("Times 10 bold",12),background="gray")
loginLabel.place(x=450,y=75)

loginLabel = Label(root, width=10,height=3, text="Password: ",font=("Times 10 bold",12), background="gray")
loginLabel.place(x=450,y=150)

userNameEntry = Entry(root, width=35,font=("bold",10),fg="black",border=0,bg="gray")
userNameEntry.place(x=600,y=95)
userNameEntry.insert(0,'')

line1 = Frame(root,width=250,height=3).place(x=600,y=115)

passwordEntry = Entry(root, width=35,font=("bold",10),fg="black",border=0,bg="gray")
passwordEntry.place(x=600,y=170)
passwordEntry.insert(0,'')

line2 = Frame(root,width=250,height=3).place(x=600,y=190)

def loginControl():
    if userNameEntry.get() =="beyza" and passwordEntry.get()=="erdem":
        tk.messagebox.showinfo("Başarılı","true")
    else:
         tk.messagebox.showinfo("Başarılı","false")    
    

loginButton = Button(root, text="Login",width=10,font="bold",command=loginControl)
loginButton.place(x=660,y=250)


root=mainloop()

