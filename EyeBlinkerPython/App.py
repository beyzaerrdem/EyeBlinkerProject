
import tkinter as tk
from tkinter import *
import Const
from RouteController import RouteController

class App():
    def __init__(self):
        routeController = RouteController()
        routeController.LoginPage()
        print(Const.CurrentUser)
        if(Const.CurrentUser != None):
            routeController.HomePage()
        else:
            print("Hata")




if __name__ == '__main__':
    app = App()