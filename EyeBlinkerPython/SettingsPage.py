import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Database import Database
from EyeBlinker import EyeBlinker
from updatePasswordPage import UpdatePasswordPage

from updateUsernamePage import UpdateUsernamePage
class SettingsPage(tk.Tk):
    images = []
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.geometry("925x500")
        self.title("Ayarlar")
        self.configure(bg="#f2eded")
        self.resizable(False,False)
        self.canvas = tk.Canvas(self, width = 1000, height = 500)
        self.canvas.pack()
        #creating background
        image = Image.open("image\Download From CBEditz.com - 2400x2000.png")
        resize_image = image.resize((1050,500))
        img = ImageTk.PhotoImage(resize_image)
        bg = self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        SettingsPage.images.append(img)
        #creating settings page

        #creating user name
        updateUsernameBtn = Button(self,width=22,height=1,text="Kullanıcı adımı güncelle",bg="#bad6ef",activebackground="#bad6ef",bd=0, command=lambda: self.openUpdateUsernameForm())
        updateUsernameBtn .place(x=370,y=100)

        updatePasswordBtn = Button(self,width=22,height=1,text="Şifremi güncelle",bg="#bad6ef",activebackground="#bad6ef",bd=0, command=lambda: self.openUpdatePasswordForm())
        updatePasswordBtn.place(x=370,y=160)

        updateEyeBlinkBtn = Button(self,width=22,height=1,text="Göz kırpma sayımı güncelle",bg="#bad6ef",activebackground="#bad6ef",bd=0,command= lambda: self.updateEyeBlinkCount())
        updateEyeBlinkBtn.place(x=370,y=220)

        deleteAccountBtn = Button(self,width=22,height=1,text="Hesabımı Sil",bg="#bad6ef",activebackground="#bad6ef",bd=0,command=lambda: self.deleteAccount())
        deleteAccountBtn.place(x=370,y=280)
        
        backPageImage = ImageTk.PhotoImage(Image.open("image\icons8-shutdown-100.png"))
        backPageButton = self.canvas.create_image(870, 50, image=backPageImage)
        self.canvas.tag_bind(backPageButton, "<Button-1>",lambda e: self.destroy())
        SettingsPage.images.append(backPageImage)


        #creating button which supports png transparency
        quitImage = ImageTk.PhotoImage(Image.open("image\icons8-go-back-100.png"))
        quitButton = self.canvas.create_image(50, 50, image=quitImage)
        self.canvas.tag_bind(quitButton, "<Button-1>", lambda e: self.back())
        SettingsPage.images.append(quitImage)
        
    def back(self):
        self.destroy()
        self.controller.HomePage()
        
        
    def openUpdateUsernameForm(self):
        self.destroy()
        updateUsernamePage = UpdateUsernamePage()
        updateUsernamePage.mainloop()
        self.controller.SettingsPage()
        
    def deleteAccount(self):
        database = Database()
        database.Delete()
        self.destroy()
        self.controller.LoginPage()
        
    def updateEyeBlinkCount(self):
        eyeBlinker = EyeBlinker(True)
        eyeBlinker.start()

    def openUpdatePasswordForm(self):
        self.destroy()
        updatePasswordPage = UpdatePasswordPage()
        updatePasswordPage.mainloop()
        self.controller.SettingsPage()
