from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class Model:
    # Active tabs
    def __init__(self):
        print(QSqlDatabase.drivers())
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("LIBRASYS.db")
        # Open the connection
        if self.con.open():
            print("Data Base connection successfull")
            query = QSqlQuery()

            name = "Linda"
            job = "Technical Lead"
            email = "linda@example.com"
            '''
            query.exec(
                """
                CREATE TABLE contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name VARCHAR(40) NOT NULL,
                    job VARCHAR(50),
                    email VARCHAR(40) NOT NULL
                )
                """
            )  
            '''
            print(self.con.tables())

