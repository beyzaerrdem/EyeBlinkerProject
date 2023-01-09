import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from Database import Database

    
class UpdateUsernamePage(tk.Tk):
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
        UpdateUsernamePage.images.append(img)
        bg = self.canvas.create_image(0, 0, image=img, anchor=tk.NW)


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


        updateUsernameButton = Button(self, text="Giriş Yap",width=10,font="bold",command=self.updateUsername,bg="#f2bceb",bd=0)
        updateUsernameButton.place(x=660,y=310)

    def updateUsername(self):
        database = Database()
        userName = self.NameEntry.get()
        if(database.UpdateUserName(userName)):
            self.destroy()
            messagebox.showinfo(message="Kullanıcı adınız başarı ile güncellendi !",title="Başarılı")

