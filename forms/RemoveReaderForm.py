# importing libraries
from .Form import Form

from PyQt5.QtWidgets import QComboBox, QLineEdit, QFormLayout, QLabel
 
# creating a class
# that inherits the QDialog class
class RemoveReaderForm(Form):
 
    # constructor
    def __init__(self):
        super().__init__("Удалить читателя", "Заполните форму:")
 
        self.libCardId = QLineEdit()

        self.createForm()
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        layout.addRow(QLabel("Номер читательского билета"), self.libCardId)
 
        # setting layout
        self.formGroupBox.setLayout(layout)