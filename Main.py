import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from MainWindow import *


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(575)
widget.setFixedWidth(840)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")