# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QLineEdit, QFormLayout, QLabel

# creating a class
# that inherits the QDialog class
class AcceptForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Принять книгу", "Заполните форму:")
 
        self.bookName = QLineEdit()


        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Название книги"), self.bookName)
 

        # setting layout
        self.formGroupBox.setLayout(layout)