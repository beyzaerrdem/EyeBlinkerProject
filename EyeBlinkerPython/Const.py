CurrentUser: dict = None
def setCurrentUser(user):
    global CurrentUser
    CurrentUser = user
def getCurrentUserAttribute(attribute):
    global CurrentUser
    return CurrentUser[attribute]
def setCurrentUserAttribute(attribute,value):
    global CurrentUser
    CurrentUser[attribute] = value