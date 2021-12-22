# from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication
import sys

# SERVER_NAME = 'LAPTOP-T9H1AR8N\SQLEXPRESS'
# DATABASE_NAME = 'DBLibrary'
# USERNAME = ''
# PASSWORD = ''

# def createConnection():
#         connString = f'DRIVER={{SQL Server}};'\
#                      f'SERVER={SERVER_NAME};'\
#                      f'DRIVER={DATABASE_NAME};'

#         global db
#         db = QSqlDatabase.addDatabase("QODBC")
#         db.setDatabaseName(connString)
#         if db.open(): 
#                 print("opened")
#                 return True
#         else:
#                 print('false')
#                 return False

# if __name__ == "__main__":
#         app = QApplication(sys.argv)
#         createConnection()

from PyQt5.QtSql import QSqlDatabase

def createConnection():
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("dblibrary.db")
        # Open the connection
        if con.open():
                print("УРА БЛЯ")
        

createConnection()