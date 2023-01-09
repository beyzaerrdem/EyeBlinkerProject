import sqlite3 as sql

from Const import getCurrentUserAttribute, setCurrentUser, setCurrentUserAttribute

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.CreateDatabase()

    def CreateConnection(self):
        self.conn=sql.connect('./DB/EyeBlinker.db')
        self.cursor = self.conn.cursor()
    def CreateDatabase(self):
        self.CreateConnection()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            UserName TEXT,
            Password TEXT,
            Mail TEXT,
            EyeBlinkCount INTEGER
             )""")
        
        self.conn.commit()
        self.conn.close()

    def Insert(self,UserName,Password,Mail):
        self.CreateConnection()
        addCommand = """INSERT INTO user (userName,password,mail,eyeBlinkCount) VALUES {};"""
        data = (UserName,Password,Mail,20)
        self.cursor.execute(addCommand.format(data))
        
        self.conn.commit()
        self.conn.close()
        return True

    def InsertEyeBlinkCount(self,eyeBlinkCount):
        self.CreateConnection()
        addEBCommand = """UPDATE user SET eyeBlinkCount = {} WHERE Id = {};"""
        self.cursor.execute(addEBCommand.format(eyeBlinkCount,getCurrentUserAttribute('Id')))
        self.conn.commit()
        self.conn.close()
        setCurrentUserAttribute('EyeBlinkCount',eyeBlinkCount)

    def UpdatePassword(self,NewPassword):
        self.CreateConnection()
        Id = getCurrentUserAttribute('Id')
        updateCommand = """UPDATE user SET password='{}' WHERE Id='{}' """
        self.cursor.execute(updateCommand.format(NewPassword,Id))
        
        self.conn.commit()
        self.conn.close()
        return True


    def UpdateUserName(self,NewUserName):
        self.CreateConnection()
        Id = getCurrentUserAttribute('Id')
        updateCommand = """UPDATE user SET userName='{}' WHERE Id='{}' """
        self.cursor.execute(updateCommand.format(NewUserName,Id))
        
        self.conn.commit()
        self.conn.close()
        return True

    def Delete(self):
        self.CreateConnection()
        Id = getCurrentUserAttribute('Id')
        deleteCommand = """DELETE FROM user WHERE Id='{}' """
        self.cursor.execute(deleteCommand.format(Id))
        
        self.conn.commit()
        self.conn.close()
        return True

    def RowFactory(self,cursor,row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    def Login(self,UserName,Password):
        self.CreateConnection()
        self.cursor.row_factory = self.RowFactory
        loginCommand = """SELECT * FROM user WHERE userName='{}' AND password='{}' """
        self.cursor.execute(loginCommand.format(UserName,Password))
        user = self.cursor.fetchone()
        self.conn.close()
        setCurrentUser(user)
        return user is not None