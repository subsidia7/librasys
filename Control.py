from forms import AddBookForm, AddReaderForm, AddIssueForm, AcceptForm
from PyQt5.QtSql import QSqlQuery


class Controller:
    def __init__(self, model, view):
        self.MODEL = model
        self.VIEW = view
        self.set_triggers()
    
    def set_triggers(self):
        # file actions
        self.VIEW._issuing_action.triggered.connect(self.issue_book)
        self.VIEW._accepting_action.triggered.connect(self.accept_book)
        self.VIEW._add_book_action.triggered.connect(self.add_book)
        self.VIEW._add_reader_action.triggered.connect(self.add_reader)
        self.VIEW._delete_book_action.triggered.connect(self.delete_book)
        self.VIEW._delete_reader_action.triggered.connect(self.delete_reader)

    def add_book(self):
        self.VIEW.bf = AddBookForm.AddBookForm()
        self.VIEW.bf.buttonBox.accepted.connect(self.add_book_to_db)
        self.VIEW.bf.show()

    def add_book_to_db(self):
        query = QSqlQuery()
        name = self.VIEW.bf.nameLineEdit.text()        
        print(query.exec(
                f"""INSERT INTO BOOK (name)
                VALUES ('{name}')"""
            ))
        self.VIEW.bf.close()


    def add_reader(self):
        self.VIEW.rf = AddReaderForm.AddReaderForm()
        self.VIEW.rf.buttonBox.accepted.connect(self.add_reader_to_db)
        self.VIEW.rf.show()

    def add_reader_to_db(self):
        query = QSqlQuery()
        name = self.VIEW.rf.nameLineEdit.text()        
        print(query.exec(
                f"""INSERT INTO BOOK (name)
                VALUES ('{name}')"""
            ))
        self.VIEW.rf.close()


    def delete_book(self):
        pass

    def delete_reader(self):
        pass

    def issue_book(self):
        self.VIEW.isf = AddIssueForm.AddIssueForm()
        self.VIEW.isf.buttonBox.accepted.connect(self.add_issue_to_db)
        self.VIEW.isf.show()

    def add_issue_to_db(self):
        query = QSqlQuery()
        name = self.VIEW.isf.nameLineEdit.text()        
        print(query.exec(
                f"""INSERT INTO BOOK (name)
                VALUES ('{name}')"""
            ))
        self.VIEW.isf.close()

    def accept_book(self):
        self.VIEW.abf = AcceptForm.AcceptForm()
        self.VIEW.abf.buttonBox.accepted.connect(self.accept_book_in_db)
        self.VIEW.abf.show()

    def accept_book_in_db(self):
        query = QSqlQuery()
        name = self.VIEW.isf.nameLineEdit.text()        
        print(query.exec(
                f"""INSERT INTO BOOK (name)
                VALUES ('{name}')"""
            ))
        self.VIEW.abf.close()

    