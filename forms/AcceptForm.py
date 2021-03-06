# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QDateEdit, QLineEdit, QFormLayout, QLabel

# creating a class
# that inherits the QDialog class
class AcceptForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Принять книгу", "Заполните форму:")
 
        self.bookId = QLineEdit()
        self.libCardId = QLineEdit()
        self.dateOfAccept = QDateEdit()


        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Код книги"), self.bookId)

        # adding rows
        layout.addRow(QLabel("Номер читательского билета"), self.libCardId)

        # adding rows
        layout.addRow(QLabel("Дата приема"), self.dateOfAccept)

        # setting layout
        self.formGroupBox.setLayout(layout)