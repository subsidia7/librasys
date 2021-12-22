# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QDateEdit, QLineEdit, QFormLayout, QLabel
 
 
# creating a class
# that inherits the QDialog class
class AddIssueForm(Form):
 
   # constructor
    def __init__(self):
        super().__init__("Выдать книгу", "Заполните форму:")
 
        self.bookCode = QLineEdit()
 
        self.readernum = QLineEdit()

        self.indate = QDateEdit()

        self.deadlinedate = QDateEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Код книги"), self.bookCode)
 
        layout.addRow(QLabel("Номер читательского билета"), self.readernum)
        
        layout.addRow(QLabel("Дата выдачи"), self.indate)

        layout.addRow(QLabel("Срок сдачи"), self.deadlinedate)


        # setting layout
        self.formGroupBox.setLayout(layout)