from PyQt5 import QtWidgets,QtGui,QtCore,uic
import sys 
from matrix import Matrix
from driver import Ui_MainWindow
import json 
from ast import literal_eval
from time import sleep
import os 


class MatrixDriver(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MatrixDriver, self).__init__(parent)
        # self.matrix = Matrix()
        self.dirpath = QtCore.QDir.currentPath()
        self.filter_name = 'All files (*.json*)'
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.addMatrixPushButton.clicked.connect(self.addMatrix)

        self.lockConfigPushButton.clicked.connect(self.lockConfig)
        self.generateConfigPushButton.clicked.connect(self.generateConfig)
        self.loadMatrix.clicked.connect(self.loadMatrixConfigFile)
        
        self.closeButton.clicked.connect(self.mainWindowClosing) # type: ignore
        self.matrixLayout = {}
        self.matrixIndex = 0
        with open(os.path.join(os.path.dirname(__file__),'styles/scrollAreaFrame.qss'), 'r') as file:
            self.scrollArea.setStyleSheet(file.read())
    def mainWindowClosing(self):
        for _,matrix in self.matrixLayout.items():
            sleep(1)
            matrix.locked = True
            matrix.freezeLineEdit()
        self.close()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # handle the left-button press in here
             self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x()+delta.x(),self.y() + delta.y())
        self.oldPosition = event.globalPos()
        
    def addMatrix(self):
        
        self.matrixLayout.update({
            self.matrixIndex : Matrix(deviceAddress=0x20+self.matrixIndex*4)
        })
        self.scrollAreaContentsverticalLayout.addWidget(list(self.matrixLayout.values())[-1])
        self.matrixIndex += 1 
        
    def lockConfig(self):
        if checked := self.lockConfigPushButton.isChecked() :
            for lineEdit  in list(self.matrixLayout.values()):
                lineEdit.locked = False
                lineEdit.freezeLineEdit()
                
        else:
            for lineEdit  in list(self.matrixLayout.values()):
                lineEdit.locked = True
                lineEdit.freezeLineEdit()
            
    
    def generateConfig(self):
        if not self.lockConfigPushButton.isChecked() :
            filepath = self.configfileImport.text()
            directory, filename = os.path.split(filepath)
            if not filename and not directory :
                filepath = os.path.join(self.dirpath,'signalroot.json')
            elif not filename:
                filepath = os.path.join(directory,'signalroot.json')
                
            SignalConfig = {}
            for index,matrix  in self.matrixLayout.items():
                SignalConfig.update(
                    {
                        index:matrix.getConfig()
                    }
                )
            with open(filepath,'w') as file :
                json.dump(SignalConfig,file)
    
    def loadMatrixConfigFile(self):
        self.matrixConfig_FileName = QtWidgets.QFileDialog.getOpenFileName(self, caption='Choose File',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name)[0]
        self.configfileImport.setText(self.matrixConfig_FileName)
        try:
            with open(self.matrixConfig_FileName, 'r') as file:
                matrixconfig = json.load(file)
                for matrix in matrixconfig.keys():
                    self.addMatrix()
                    for path,data in matrixconfig.get(matrix).items():
                        self.matrixLayout[literal_eval(matrix)].setSignalText(data=literal_eval(path), relay=data.get('relay'))
        except :
            print('File is not loaded')
            
def MatrixDriver_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = MatrixDriver()
    with open(os.path.join(os.path.dirname(__file__),'styles/app.qss'),"r") as appStyles :
        app.setStyleSheet(appStyles.read())
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MatrixDriver()
    with open(os.path.join(os.path.dirname(__file__),'styles/app.qss'),"r") as appStyles :
        app.setStyleSheet(appStyles.read())
    window.show()
    sys.exit(app.exec())
