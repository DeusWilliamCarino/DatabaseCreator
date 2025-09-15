from module import dbmodules as useModule

import json

from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QVBoxLayout, QLabel,QHBoxLayout,QTextEdit, QMessageBox,QLineEdit

import sys



with open('data/buttonDetails.json', 'r') as f:
    buttonDetails  = json.load(f)



toBeGenerated = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.selectedButton = ""
        self.setWindowTitle("Database Creator")
        
        mainLabel = QLabel("Database Creator")
        mainLabelFont = mainLabel.font()
        mainLabelFont.setPointSize(30)
        mainLabel.setFont(mainLabelFont)
        mainLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        titlebar = QVBoxLayout()
        titlebar.addWidget(mainLabel)

        #=======================================#

        self.namebtn = QPushButton("Names")
        self.namebtn.clicked.connect(lambda:self.clicked_Button("Names",infoOfButton))
        self.nameFXbtn = QPushButton("Names (Fixed)")
        self.nameFXbtn.clicked.connect(lambda:self.clicked_Button("Names (Fixed)",infoOfButton))

        self.countrybtn = QPushButton("Country")
        self.countrybtn.clicked.connect(lambda:self.clicked_Button("Country",infoOfButton))

        self.genderbtn = QPushButton("Gender")
        self.genderbtn.clicked.connect(lambda:self.clicked_Button("Gender",infoOfButton))



        self.selectedData = QTextEdit()
        self.selectedData.setPlaceholderText("No Data Chosen Yet")
        self.selectedData.setReadOnly(True)

        selectedDataLayout = QVBoxLayout()
        selectedDataLayout.addWidget(self.selectedData)
        
        buttonSelectorLayout = QHBoxLayout()
        buttonSelectorLayout.addWidget(self.namebtn)
        buttonSelectorLayout.addWidget(self.nameFXbtn)
        buttonSelectorLayout.addWidget(self.countrybtn)
        buttonSelectorLayout.addWidget(self.genderbtn)


        generatebtn = QPushButton("Generate Database")
        generatebtn.clicked.connect(lambda:self.generateDBButton())

        self.numOfEntry = QLineEdit()
        self.numOfEntry.setMaxLength(7)
        self.numOfEntry.setPlaceholderText("Enter the maximum number of entry you need")
        self.numOfEntry.setValidator(QIntValidator())

        labelOfEntry = QLabel("Max Entry: ")
        labelOfEntry.setAlignment(Qt.AlignmentFlag.AlignLeft)

        entryDataLayout = QHBoxLayout()
        entryDataLayout.addWidget(labelOfEntry)
        entryDataLayout.addWidget(self.numOfEntry)

        buttonNSelectionLayout = QVBoxLayout()
        buttonNSelectionLayout.addLayout(buttonSelectorLayout)
        buttonNSelectionLayout.addLayout(selectedDataLayout)
        buttonNSelectionLayout.addLayout(entryDataLayout)
        buttonNSelectionLayout.addWidget(generatebtn)

        #=======================================#

        infoOfButton = QTextEdit()
        infoOfButton.setPlaceholderText("Select A Button To try")
        infoOfButton.setReadOnly(True)

        addBtn = QPushButton("Add")
        addBtn.clicked.connect(lambda:self.addButtonFunc(self.selectedButton))
        remBtn = QPushButton("Remove")
        remBtn.clicked.connect(lambda:self.remButtonFunc(self.selectedButton))

        infoSelectedBttnLayout = QHBoxLayout()
        infoSelectedBttnLayout.addWidget(addBtn)
        infoSelectedBttnLayout.addWidget(remBtn)


        infoSelectedLayout = QVBoxLayout()
        infoSelectedLayout.addWidget(infoOfButton)
        infoSelectedLayout.addLayout(infoSelectedBttnLayout)
        #=======================================#

        selectionArea = QHBoxLayout()
        selectionArea.addLayout(buttonNSelectionLayout)
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
        self.selectedButton = name

    def addButtonFunc(self,name):
        result = useModule.addToBeGenerated(name,toBeGenerated)

        if name == "Names (Fixed)":
            self.namebtn.setDisabled(True)
            useModule.removeToBeGenerated("Names",toBeGenerated)

        if result == "Its already chosen":
            QMessageBox.critical(self,"Duplicate Entry!",result,buttons=QMessageBox.StandardButton.Ok)
        self.changeSelectedData()
        

    def remButtonFunc(self,name):
        result = useModule.removeToBeGenerated(name,toBeGenerated)
        
        if result == "It has not been chosen yet":
             QMessageBox.critical(self,"Not Found!",result,buttons=QMessageBox.StandardButton.Ok)
        else:
            if name == "Names (Fixed)":
                self.namebtn.setDisabled(False)

        self.changeSelectedData()
        
    def changeSelectedData(self):
        if not toBeGenerated:
            self.selectedData.setText("No data has been chosen")
        else:
            placer = "|"
            for x in toBeGenerated:
                placer += x + "|"
            self.selectedData.setText(placer)

    def generateDBButton(self):
        entryNum = self.numOfEntry.text()
        if entryNum == "":
            QMessageBox.critical(self,"No number inputted","Enter a number of data to be generated",buttons=QMessageBox.StandardButton.Ok)
        elif toBeGenerated == []:
            QMessageBox.critical(self,"No columns chosen","Enter columns to be generated",buttons=QMessageBox.StandardButton.Ok)
        else:
            useModule.createDB(entryNum,toBeGenerated)
    



app = QApplication(sys.argv)
window = MainWindow()
window.show() 

app.exec()