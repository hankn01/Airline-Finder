import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#라이브러리

form_class = uic.loadUiType("메인 화면.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
