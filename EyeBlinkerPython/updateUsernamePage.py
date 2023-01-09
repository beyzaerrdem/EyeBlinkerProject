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
        
        Label(self,text="Kullanıcı Adınızı Güncelleyin",font=("Times 10 bold",15),bg="#bad6ef").place(x=385,y=70)

        userNameLabel = Label(self, width=16,height=1, text="Yeni Kullanıcı Adınız: ",font=("Times 10 bold",12), bg="#bad6ef")
        userNameLabel.place(x=230,y=200)

        self.NameEntry = Entry(self, width=35,font=("bold",10),fg="black",border=0,bg="#bad6ef")
        self.NameEntry.place(x=390,y=200)
        self.NameEntry.insert(0,'')

        usernameline = Frame(self,width=250,height=3,bg="gray").place(x=390,y=220)

        updateUsernameButton = Button(self, text="Kullanıcı Adımı Güncelle",width=20,font=("bold",10),command=self.updateUsername,bg="#bad6ef",bd=0)
        updateUsernameButton.place(x=430,y=310)
        
        
        quitImage = ImageTk.PhotoImage(Image.open("image\icons8-go-back-100.png"))
        quitButton = self.canvas.create_image(50, 50, image=quitImage)
        self.canvas.tag_bind(quitButton, "<Button-1>", lambda e: self.back())
        UpdateUsernamePage.images.append(quitImage)
        
    def back(self):
        self.destroy()
        self.controller.SettingsPage()    

    def updateUsername(self):
        database = Database()
        userName = self.NameEntry.get()
        if(database.UpdateUserName(userName)):
            self.destroy()
            messagebox.showinfo(message="Kullanıcı adınız başarı ile güncellendi !",title="Başarılı")

