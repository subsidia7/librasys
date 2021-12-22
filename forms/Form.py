# importing libraries
from PyQt5.QtWidgets import QDialog, QGroupBox, QSpinBox, QComboBox, QLineEdit, QDialogButtonBox, QVBoxLayout, QFormLayout, QLabel, QDesktopWidget
import sys
 
# creating a class
# that inherits the QDialog class
class Form(QDialog):
 
    # constructor
    def __init__(self, title, BoxName):
        super(Form, self).__init__()
 
        # setting window title
        self.setWindowTitle(title)
 
        # setting geometry to the window
        self.setGeometry(100, 100, 600, 400)
 
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # creating a group box
        self.formGroupBox = QGroupBox(BoxName)
 
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