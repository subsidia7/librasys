from PyQt5.QtSql import QSqlDatabase

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName(
"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\\Library.accdb")
if db.open(): 
	print("opened")
else:
	print("not")