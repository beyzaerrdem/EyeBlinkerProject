import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from Database import Database

    
class UpdatePasswordPage(tk.Tk):
    images = []
    def __init__(self):
        super().__init__()
        self.title("Kullanıcı Adı Güncelle")
        self.geometry("925x500")
        self.configure(bg="#f2eded")
        self.resizable(False,False)

        self.canvas = tk.Canvas(self, width = 1000, height = 500)
        self.canvas.pack()
        #creating background
        image = Image.open("image\Download From CBEditz.com - 2400x2000.png")
        resize_image = image.resize((1050,500))
        img = ImageTk.PhotoImage(resize_image)
        bg = self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        UpdatePasswordPage.images.append(img)

        loginLabel = Label(self, width=10,height=3, text="UserName: ",font=("Times 10 bold",12),background="#f2eded")
        loginLabel.place(x=500,y=120)

        pLabel = Label(self, width=10,height=3, text="Password: ",font=("Times 10 bold",12), background="#f2eded")
        pLabel.place(x=500,y=200)

        self.NameEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.NameEntry.place(x=600,y=140)
        self.NameEntry.insert(0,'')

        line1 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=160)

        self.PasswordEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#f2eded")
        self.PasswordEntry.place(x=600,y=220)
        self.PasswordEntry.insert(0,'')

        line2 = Frame(self,width=250,height=3,bg="gray").place(x=600,y=240)


        updatePasswordButton = Button(self, text="Şifreyi Güncelle",width=10,font="bold",command=self.updatePassword,bg="#f2bceb",bd=0)
        updatePasswordButton.place(x=660,y=310)

    def updatePassword(self):
        database = Database()
        password = self.PasswordEntry.get()
        if(database.UpdatePassword(password)):
            self.destroy()
            messagebox.showinfo(message="Şifreniz başarı ile güncellendi !",title="Başarılı")

