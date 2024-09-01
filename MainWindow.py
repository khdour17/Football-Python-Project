from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from League import *
from LeagueDataLoader import league
from SearchScreen import * 

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui",self)
        self.tableWidget.setColumnWidth(0,158)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,50)
        self.tableWidget.setColumnWidth(4,50)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,50)
        self.tableWidget.setColumnWidth(7,50)
        self.tableWidget.setColumnWidth(8,50)
        self.LoadTableData()
        self.SimulateButton.clicked.connect(self.Simulation)
        self.ResetButton.clicked.connect(self.Reset)
        self.SearchButton.clicked.connect(self.openSearchWindow)
    
    def LoadTableData(self):
        league.displayTable(self.tableWidget)

    def Simulation(self):
        league.resetStats()
        self.RoundResultLog.clear() 
        self.GoalsScorersLog.clear()  
        self.tableWidget.clearContents()
        league.simulateRounds(self.RoundResultLog)
        league.displayTopScorers(5,self.GoalsScorersLog)
        self.LoadTableData()
    
    def Reset(self):
        league.resetStats()
        self.RoundResultLog.clear() 
        self.GoalsScorersLog.clear()  
        self.tableWidget.clearContents()
        self.LoadTableData()
    
    def openSearchWindow(self):
        self.window = SearchScreen()
        self.window.show()