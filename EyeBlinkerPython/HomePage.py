import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from EyeBlinker import EyeBlinker



class HomePage(tk.Tk):
    images = []
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Anasayfa")
        self.geometry("925x500")
        self.resizable(False,False)
        self.canvas = Canvas(self, width = 1000, height = 500)
        self.canvas.pack()

        #creating background
        image = Image.open("image\Download From CBEditz.com - 2400x2000.png")
        resize_image = image.resize((1050,500))

        img = ImageTk.PhotoImage(resize_image)
        bg = self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        HomePage.images.append(img)

        saglikLabel=Label(self,width=70,height=7 ,font=("bold",9),background="#bad6ef", text="\n Göz kırpma sayısı, kişiden kişiye değişebilir ancak genellikle, \n  bir dakikalık süre içinde 15-20 kez göz kırpmak gözlerin yeterince nemlenmesini sağlar.\n Başlat butonuna tıkladığınızda bu sayı geçerli olur. \n Eğer bir dakikalık süredeki göz kırpma sayınızı özelleştirmek istiyorsanız \n  ayarlar sayfasından göz kırpma sayınızı güncelleyebilirsiniz.\n")
        saglikLabel.place(x=180,y=80)

        #creating button which supports png transparency
        quitImage = ImageTk.PhotoImage(Image.open("image\icons8-shutdown-100.png"))
        quitButton = self.canvas.create_image(870, 50, image=quitImage)
        self.canvas.tag_bind(quitButton, "<Button-1>", lambda e: self.destroy())
        HomePage.images.append(quitImage)

        settingImage = ImageTk.PhotoImage(Image.open("image\icons8-gear-200.png"))
        settingButton = self.canvas.create_image(870, 150, image=settingImage)
        self.canvas.tag_bind(settingButton, "<Button-1>", lambda e: self.settingsPage())
        HomePage.images.append(settingImage)

        startBtn = Button(self,width=30,font=("bold",9),background="#bad6ef",bd=0, text="BAŞLAT",command=self.start)
        startBtn.place(x=350,y=350)

    def start(self):
        self.destroy()
        eyeBlinker = EyeBlinker()
        eyeBlinker.start()

    def settingsPage(self):
        self.destroy()
        self.controller.SettingsPage()

if __name__ == "__main__":
    homePage = HomePage()
    homePage.mainloop()