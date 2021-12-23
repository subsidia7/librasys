from forms import AddBookForm, AddReaderForm, AddIssueForm, AcceptForm, RemoveReaderForm, RemoveBookForm
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QTableWidgetItem
from Constants import FINE_PER_DAY
import datetime


class Controller:
    def __init__(self, model, view):
        self.MODEL = model
        self.VIEW = view
        self.load_data()
        self.set_triggers()
    
    def load_data(self):
        self.load_books()
        self.load_readers()
        self.load_issues()

    def load_books(self):
        self.VIEW.books_table.setRowCount(0)
        query = QSqlQuery("SELECT id, name, authors, pubyear, place, fondnum, udk, bbk, amount FROM Books")
        while query.next():
            rows = self.VIEW.books_table.rowCount()
            self.VIEW.books_table.setRowCount(rows + 1)
            self.VIEW.books_table.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.VIEW.books_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.VIEW.books_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.VIEW.books_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
            self.VIEW.books_table.setItem(rows, 4, QTableWidgetItem(str(query.value(4))))
            self.VIEW.books_table.setItem(rows, 5, QTableWidgetItem(str(query.value(5))))
            self.VIEW.books_table.setItem(rows, 6, QTableWidgetItem(str(query.value(6))))
            self.VIEW.books_table.setItem(rows, 7, QTableWidgetItem(str(query.value(7))))
            self.VIEW.books_table.setItem(rows, 8, QTableWidgetItem(str(query.value(8))))
        self.VIEW.books_table.resizeColumnsToContents()


    def load_readers(self):
        self.VIEW.readers_table.setRowCount(0)
        query = QSqlQuery("SELECT Lib_card_id, last_name, first_name, patronymic, passport_id, address, phone_number, fine FROM Readers")
        while query.next():
            rows = self.VIEW.readers_table.rowCount()
            self.VIEW.readers_table.setRowCount(rows + 1)
            self.VIEW.readers_table.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.VIEW.readers_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.VIEW.readers_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.VIEW.readers_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
            self.VIEW.readers_table.setItem(rows, 4, QTableWidgetItem(str(query.value(4))))
            self.VIEW.readers_table.setItem(rows, 5, QTableWidgetItem(str(query.value(5))))
            self.VIEW.readers_table.setItem(rows, 6, QTableWidgetItem(str(query.value(6))))
            self.VIEW.readers_table.setItem(rows, 7, QTableWidgetItem(str(query.value(7))))
        self.VIEW.readers_table.resizeColumnsToContents()


    def load_issues(self):
        self.VIEW.issues_table.setRowCount(0)
        query = QSqlQuery("SELECT issue_id, book_id, lib_card_id, date_of_issue, dead_line FROM Issues")
        while query.next():
            rows = self.VIEW.issues_table.rowCount()
            self.VIEW.issues_table.setRowCount(rows + 1)
            self.VIEW.issues_table.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.VIEW.issues_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.VIEW.issues_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.VIEW.issues_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
        self.VIEW.issues_table.resizeColumnsToContents()


    def set_triggers(self):
        # file actions
        self.VIEW._issuing_action.triggered.connect(self.issue_book)
        self.VIEW._accepting_action.triggered.connect(self.accept_book)
        self.VIEW._add_book_action.triggered.connect(self.add_book)
        self.VIEW._add_reader_action.triggered.connect(self.add_reader)
        self.VIEW._delete_book_action.triggered.connect(self.delete_book)
        self.VIEW._delete_reader_action.triggered.connect(self.delete_reader)
        self.VIEW._update_tables_action.triggered.connect(self.load_data)

    def add_book(self):
        self.VIEW.bf = AddBookForm.AddBookForm()
        self.VIEW.bf.buttonBox.accepted.connect(self.add_book_to_db)
        self.VIEW.bf.show()

    def add_book_to_db(self):
        query = QSqlQuery()
        book_name = self.VIEW.bf.bookName.text()        
        authors = self.VIEW.bf.authors.text()        
        year = self.VIEW.bf.year.text()     
        place = self.VIEW.bf.place.text()        
        fondnum = self.VIEW.bf.fondnum.text()        
        udk = self.VIEW.bf.udk.text()        
        bbk = self.VIEW.bf.bbk.text()   
        amount = self.VIEW.bf.amount.text()      
        
        print(query.exec(
                f"""INSERT INTO Books (name, authors, pubyear, place, fondnum, udk, bbk, amount)
                VALUES ('{book_name}', '{authors}', {year}, '{place}', {fondnum}, {udk}, '{bbk}',
            {amount})"""
            ))
        self.VIEW.bf.close()


    def add_reader(self):
        self.VIEW.rf = AddReaderForm.AddReaderForm()
        self.VIEW.rf.buttonBox.accepted.connect(self.add_reader_to_db)
        self.VIEW.rf.show()

    def add_reader_to_db(self):
        query = QSqlQuery()
        last_name = self.VIEW.rf.lastName.text()
        first_name = self.VIEW.rf.firstName.text()  
        patronymic = self.VIEW.rf.patronymic.text()
        passport_id = self.VIEW.rf.passportId.text() 
        address = self.VIEW.rf.address.text()
        phone_number = self.VIEW.rf.phoneNumber.text()   
        fine = 0  
        print(query.exec(
                f"""INSERT INTO Readers (last_name, first_name, patronymic, passport_id, address, phone_number, fine)
                VALUES ('{last_name}', '{first_name}', '{patronymic}', {passport_id}, '{address}', '{phone_number}', {fine})"""
            ))
        self.VIEW.rf.close()


    def delete_book(self):
            self.VIEW.dbf = RemoveBookForm.RemoveBookForm()
            self.VIEW.dbf.buttonBox.accepted.connect(self.delete_book_from_db)
            self.VIEW.dbf.show()

    def delete_book_from_db(self):
        query = QSqlQuery()
        book_id = self.VIEW.dbf.bookId.text()
        print("BOOK deleting = ", query.exec(f"DELETE FROM Books WHERE id = {book_id}"))

        self.VIEW.dbf.close()

    def delete_reader(self):
            self.VIEW.drf = RemoveReaderForm.RemoveReaderForm()
            self.VIEW.drf.buttonBox.accepted.connect(self.delete_reader_from_db)
            self.VIEW.drf.show()

    def delete_reader_from_db(self):
        query = QSqlQuery()
        lib_card_id = self.VIEW.drf.libCardId.text()
        print("READER deleting = ", query.exec(f"DELETE FROM Readers WHERE lib_card_id = {lib_card_id}"))

        self.VIEW.drf.close()

    def issue_book(self):
        self.VIEW.isf = AddIssueForm.AddIssueForm()
        self.VIEW.isf.buttonBox.accepted.connect(self.add_issue_to_db)
        self.VIEW.isf.show()

    def add_issue_to_db(self):
        query = QSqlQuery()
        book_id = self.VIEW.isf.bookId.text()
        lib_card_id = self.VIEW.isf.libCardId.text() 
        date_of_issue = self.VIEW.isf.dateOfIssue.text()
        dead_line = self.VIEW.isf.deadLine.text() 
        
        print("ISSUE Adding = ", query.exec(
                f"""INSERT INTO Issues (book_id, lib_card_id, date_of_issue, dead_line)
                VALUES ('{book_id}', '{lib_card_id}', '{date_of_issue}', '{dead_line}')"""
            ))

        query.exec(f"SELECT amount FROM Books WHERE id = {book_id}")
        query.next()
        amount = query.value(0)
        #print("AMOUNT = ", amount)

        print("AMOUNT Updating = ", query.exec(
                f"UPDATE Books SET amount = {amount - 1} WHERE id = {book_id}"
            ))
        
        self.VIEW.isf.close()

    def accept_book(self):
        self.VIEW.abf = AcceptForm.AcceptForm()
        self.VIEW.abf.buttonBox.accepted.connect(self.accept_book_in_db)
        self.VIEW.abf.show()

    def accept_book_in_db(self):
        query = QSqlQuery()
        book_id = self.VIEW.abf.bookId.text()
        lib_card_id = self.VIEW.abf.libCardId.text()  
        date_of_accept = self.VIEW.abf.dateOfAccept.text()

        print("AMOUNT getting = ", query.exec(f"SELECT amount FROM Books WHERE id = {book_id}"))
        query.next()
        amount = query.value(0)        
        
        print("AMOUNT Updating = ", query.exec(
                f"UPDATE Books SET amount = {amount + 1} WHERE id = {book_id}"
            ))

        print("DEAD_LINE getting = ", query.exec(
            f"SELECT dead_line FROM Issues WHERE book_id = {book_id} AND lib_card_id = {lib_card_id}"
            ))
        query.next()
        dead_line = query.value(0)  
        print("DEAD_LINE = ", dead_line)
        day, month, year = dead_line.split('.')
        date_dead_line = datetime.datetime(year=int(year), month=int(month), day=int(day))
        print(date_dead_line)

        day, month, year = date_of_accept.split('.')
        date_date_of_accept = datetime.datetime(year=int(year), month=int(month), day=int(day))
        print(date_date_of_accept)

        if date_date_of_accept > date_dead_line:
            dif = date_date_of_accept - date_dead_line
            days = dif.days
            print("FINE GETTING = ", query.exec(
                f"SELECT fine FROM Readers WHERE lib_card_id = {lib_card_id}"
                ))
            query.next()
            fine = query.value(0)
            fine = days * FINE_PER_DAY + fine
            print("FINE = ", fine)
            print("FINE Updating = ", query.exec(
                    f"UPDATE Readers SET fine = {fine} WHERE lib_card_id = {lib_card_id}"
                ))

        self.VIEW.abf.close()

    