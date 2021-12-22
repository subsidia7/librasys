# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QLineEdit, QFormLayout, QLabel
 
# creating a class
# that inherits the QDialog class
class AddReaderForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Добавить читателя", "Заполните форму:")
 
        self.surname = QLineEdit()

        self.name = QLineEdit()

        self.patronymic = QLineEdit()

        self.passport = QLineEdit()

        self.address = QLineEdit()

        self.phone = QLineEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Фамилия"), self.surname)
 
        layout.addRow(QLabel("Имя"), self.name)
 
        layout.addRow(QLabel("Отчество"), self.patronymic)
 
        layout.addRow(QLabel("Номер паспорта"), self.passport)

        layout.addRow(QLabel("Адрес проживания"), self.address)

        layout.addRow(QLabel("Номер телефона"), self.phone)

        # setting layout
        self.formGroupBox.setLayout(layout)