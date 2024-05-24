from PyQt5 import QtWidgets,QtGui,QtCore,uic
import sys 
from IvmDriver.matrixDriver import MainWindow

def gui():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    with open('styles/app.qss',"r") as appStyles :
        app.setStyleSheet(appStyles.read())
    window.show()
    sys.exit(app.exec())
    
