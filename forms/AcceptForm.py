# importing libraries
from PyQt5.QtWidgets import QDialog, QGroupBox, QSpinBox, QComboBox, QLineEdit, QDialogButtonBox, QVBoxLayout, QFormLayout, QLabel
import sys
 
# creating a class
# that inherits the QDialog class
class AcceptForm(QDialog):
 
    # constructor
    def __init__(self):
        super(AcceptForm, self).__init__()
 
        # setting window title
        self.setWindowTitle("Добавить читателя")
 
        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)
 
        # creating a group box
        self.formGroupBox = QGroupBox("Form 1")
 
        # creating spin box to select age
        self.ageSpinBar = QSpinBox()
 
        # creating combo box to select degree
        self.degreeComboBox = QComboBox()
 
        # adding items to the combo box
        self.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
 
        # creating a line edit
        self.nameLineEdit = QLineEdit()
 
        # calling the method that create the form
        self.createForm()
 
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
 
        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
 
        # creating a vertical layout
        mainLayout = QVBoxLayout()
 
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
 
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
 
        # setting lay out
        self.setLayout(mainLayout)
 
    # creat form method
    def createForm(self):
 
        # creating a form layout
        layout = QFormLayout()
 
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name"), self.nameLineEdit)
 
        # for degree and adding combo box
        layout.addRow(QLabel("Degree"), self.degreeComboBox)
 
        # for age and adding spin box
        layout.addRow(QLabel("Age"), self.ageSpinBar)
 
        # setting layout
        self.formGroupBox.setLayout(layout)