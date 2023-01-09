import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import RouteController

from Database import Database

class SignUpPage(tk.Tk):
    images = []
    def __init__(self,controller):
        self.controller = controller
        super().__init__()
        self.title("SignUp")
        self.geometry("925x500")
        self.configure(bg="#f2eded")
        self.resizable(False,False)

        img = Image.open("image\signUp.png")
        resize_image = img.resize((350,350))
        SignUpPage.images.append(resize_image)

        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(self,image=img)
        label1.place(x=50,y=50)
        SignUpPage.images.append(img)

        heading = Label(self,text="Kayıt Ol",font=("Times 10 bold",20),bg="#f2eded").place(x=660,y=50)

        mailLabel = Label(self, width=10,height=3, text="Mail: ",font=("Times 10 bold",12),background="#f2eded")
        mailLabel.place(x=520,y=100)

        self.mailEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.mailEntry.place(x=600,y=120)
        self.mailEntry.insert(0,'')

        line3 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=140)

        loginLabel = Label(self, width=10,height=3, text="UserName: ",font=("Times 10 bold",12),background="#f2eded")
        loginLabel.place(x=505,y=175)

        pLabel = Label(self, width=10,height=3, text="Password: ",font=("Times 10 bold",12), background="#f2eded")
        pLabel.place(x=505,y=250)

        self.NameEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.NameEntry.place(x=600,y=195)
        self.NameEntry.insert(0,'')

        line1 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=215)

        self.passwordEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.passwordEntry.place(x=600,y=270)
        self.passwordEntry.insert(0,'')

        line2 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=290)

        loginButton = Button(self, text="Kayıt Ol",width=10,font="bold",command=self.signUp,bg="#f2bceb",bd=0)
        loginButton.place(x=660,y=310)

    def signUp(self):
        database = Database()
        if(database.Insert(self.NameEntry.get(),self.passwordEntry.get(),self.mailEntry.get())):
            self.destroy()
            messagebox.showinfo(message="Başarılı!",title="False")
            self.controller.LoginPage()
        else:
            messagebox.showinfo(message="Kullanıcı adı ya da şifre hatalı !",title="False")

        


if __name__ == "__main__":
    signUpPage = SignUpPage(RouteController.RouteController())
    signUpPage.mainloop()