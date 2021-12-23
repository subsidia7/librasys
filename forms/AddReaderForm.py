# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QLineEdit, QFormLayout, QLabel
 
# creating a class
# that inherits the QDialog class
class AddReaderForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Добавить читателя", "Заполните форму:")
 
        self.lastName = QLineEdit()

        self.firstName = QLineEdit()

        self.patronymic = QLineEdit()

        self.passportId = QLineEdit()

        self.address = QLineEdit()

        self.phoneNumber = QLineEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Фамилия"), self.lastName)
 
        layout.addRow(QLabel("Имя"), self.firstName)
 
        layout.addRow(QLabel("Отчество"), self.patronymic)
 
        layout.addRow(QLabel("Номер паспорта"), self.passportId)

        layout.addRow(QLabel("Адрес проживания"), self.address)

        layout.addRow(QLabel("Номер телефона"), self.phoneNumber)

        # setting layout
        self.formGroupBox.setLayout(layout)