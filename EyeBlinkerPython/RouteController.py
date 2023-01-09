from HomePage import HomePage
from LoginPage import LoginPage
from SettingsPage import SettingsPage


class RouteController:
    def HomePage(self):
        homePage = HomePage(self)
        homePage.mainloop()
    def SettingsPage(self):
        settingsPage = SettingsPage(self)
        settingsPage.mainloop()
    def LoginPage(self):
        loginPage = LoginPage()
        loginPage.mainloop()