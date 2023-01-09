import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from Database import Database

    
class UpdatePasswordPage(tk.Tk):
    images = []
    def __init__(self):
        super().__init__()
        self.title("Şifre Güncelle")
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

        Label(self,text="Şifrenizi Güncelleyin",font=("Times 10 bold",15),bg="#bad6ef").place(x=405,y=50)

        newpasswordLabel = Label(self, width=12, text="Yeni Şifreniz: ",font=("Times 10 bold",12),background="#bad6ef")
        newpasswordLabel.place(x=265,y=180)


        self.newPasswordEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#bad6ef")
        self.newPasswordEntry.place(x=385,y=180)
        self.newPasswordEntry.insert(0,'')

        line2 = Frame(self,width=250,height=3,bg="gray").place(x=385,y=200)


        updatePasswordButton = Button(self, text="Şifreyi Güncelle",width=15,font=("bold",10),command=self.updatePassword,bg="#bad6ef",bd=0)
        updatePasswordButton.place(x=430,y=310)
        
        quitImage = ImageTk.PhotoImage(Image.open("image\icons8-go-back-100.png"))
        quitButton = self.canvas.create_image(50, 50, image=quitImage)
        self.canvas.tag_bind(quitButton, "<Button-1>", lambda e: self.back())
        UpdatePasswordPage.images.append(quitImage)
        
    def back(self):
        self.destroy()
        self.controller.SettingsPage()    
        
    def updatePassword(self):
        database = Database()
        password = self.newPasswordEntry.get()
        if(database.UpdatePassword(password)):
            self.destroy()
            messagebox.showinfo(message="Şifreniz başarı ile güncellendi !",title="Başarılı")

