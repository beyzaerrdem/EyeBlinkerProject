import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title("Eye Blinker Sign Up")
root.geometry("925x500")
root.config(bg="#d8b8d8")
root.resizable(False,False)  #width height değiştirme kapalı


#def oneMinuteCountControl():
    #bir dakikalık sayaç tutulacak


oneMinuteCountBtn = Button(root, text="Göz kırpma sayınızı kaydedin",width=30,font=("bold",9)).place(x=300,y=350)


root=mainloop()
