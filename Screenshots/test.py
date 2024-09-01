import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        super(MainWindow,self).__init__()
        loadUi("main.ui",self)


class RoundsScreen(QtWidgets.QMainWindow):
    def __init__(self): 
        super(RoundsScreen,self).__init__()
        loadUi("RoundsScreen.ui",self)

app = QApplication()    
app.exec()