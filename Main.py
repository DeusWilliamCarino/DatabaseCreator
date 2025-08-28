from module import dbmodules as useModule

import json

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QVBoxLayout, QLabel,QHBoxLayout,QTextEdit

import sys



with open('data/buttonDetails.json', 'r') as f:
    buttonDetails  = json.load(f)


selectedButton = ""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Database Creator")
        
        mainLabel = QLabel("Dabase Creator")
        mainLabelFont = mainLabel.font()
        mainLabelFont.setPointSize(30)
        mainLabel.setFont(mainLabelFont)
        mainLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        titlebar = QVBoxLayout()
        titlebar.addWidget(mainLabel)

        #=======================================#

        namebtn = QPushButton("Names")
        namebtn.clicked.connect(lambda:self.clicked_Button("Names",infoOfButton))

        countrybtn = QPushButton("Button")
        countrybtn.clicked.connect(lambda:self.clicked_Button("Country",infoOfButton))

        genderbtn = QPushButton("Gender")
        genderbtn.clicked.connect(lambda:self.clicked_Button("Gender",infoOfButton))

        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(namebtn)
        buttonLayout.addWidget(countrybtn)
        buttonLayout.addWidget(genderbtn)

        #=======================================#

        infoOfButton = QTextEdit()
        infoOfButton.setPlaceholderText("Select A Button To try")
        infoOfButton.isReadOnly

        infoSelectedLayout = QVBoxLayout()
        infoSelectedLayout.addWidget(infoOfButton)
        #=======================================#

        selectionArea = QHBoxLayout()
        selectionArea.addLayout(buttonLayout)
        selectionArea.addLayout(infoSelectedLayout)
        #=======================================#

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(titlebar)
        mainLayout.addLayout(selectionArea)


        container = QWidget()
        container.setLayout(mainLayout)

        self.setCentralWidget(container)
        
    def clicked_Button(self,name,txtLayout):
        txtLayout.setText(buttonDetails[name])



app = QApplication(sys.argv)
window = MainWindow()
window.show() 

app.exec()