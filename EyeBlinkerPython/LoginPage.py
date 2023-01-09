import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from Database import Database


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("925x500")
        self.configure(bg="#f2eded")
        self.resizable(False,False)

        img = Image.open("image\login3.png")
        resize_image = img.resize((350,350))

        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(self,image=img)
        label1.place(x=50,y=70)
        label1.image = img

        Label(self,text="Giriş Yap",font=("Times 10 bold",20),bg="#f2eded").place(x=660,y=50)

        loginLabel = Label(self, width=10,height=3, text="UserName: ",font=("Times 10 bold",12),background="#f2eded")
        loginLabel.place(x=500,y=120)

        pLabel = Label(self, width=10,height=3, text="Password: ",font=("Times 10 bold",12), background="#f2eded")
        pLabel.place(x=500,y=200)

        self.NameEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.NameEntry.place(x=600,y=140)
        self.NameEntry.insert(0,'')

        line1 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=160)

        self.passwordEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.passwordEntry.place(x=600,y=220)
        self.passwordEntry.insert(0,'')

        line2 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=240)


        loginButton = Button(self, text="Giriş Yap",width=10,font="bold",command=self.login,bg="#f2bceb",bd=0)
        loginButton.place(x=660,y=310)

    def login(self):
        database = Database()
        userName = self.NameEntry.get()
        password = self.passwordEntry.get()
        if(database.Login(userName,password)):
            self.destroy()
        else:
            messagebox.showinfo(message="Kullanıcı adı ya da şifre hatalı !",title="False")


if __name__ == "__main__":
    loginPage = LoginPage()
    loginPage.mainloop()