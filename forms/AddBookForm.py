# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QLineEdit, QFormLayout, QLabel
 
# creating a class
# that inherits the QDialog class
class AddBookForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Добавить книгу", "Заполните форму:")
 
        self.bookName = QLineEdit()
 
        self.authors = QLineEdit()

        self.year = QLineEdit()

        self.place = QLineEdit()

        self.fondnum = QLineEdit()

        self.udk = QLineEdit()

        self.bbk = QLineEdit()

        self.amount = QLineEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Название книги"), self.bookName)
 
        layout.addRow(QLabel("Авторы"), self.authors)
 
        layout.addRow(QLabel("Год издания"), self.year)
 
        layout.addRow(QLabel("Место издания"), self.place)

        layout.addRow(QLabel("Фондовый номер"), self.fondnum)

        layout.addRow(QLabel("УДС"), self.udk)

        layout.addRow(QLabel("ББК"), self.bbk)

        layout.addRow(QLabel("Количество экземпляров"), self.amount)

        # setting layout
        self.formGroupBox.setLayout(layout)