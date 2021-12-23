# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QDateEdit, QLineEdit, QFormLayout, QLabel
 
 
# creating a class
# that inherits the QDialog class
class AddIssueForm(Form):
 
   # constructor
    def __init__(self):
        super().__init__("Выдать книгу", "Заполните форму:")
 
        self.bookId = QLineEdit()
 
        self.libCardId = QLineEdit()

        self.dateOfIssue = QDateEdit()

        self.deadLine = QDateEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Код книги"), self.bookId)
 
        layout.addRow(QLabel("Номер читательского билета"), self.libCardId)
        
        layout.addRow(QLabel("Дата выдачи"), self.dateOfIssue)

        layout.addRow(QLabel("Срок сдачи"), self.deadLine)


        # setting layout
        self.formGroupBox.setLayout(layout)