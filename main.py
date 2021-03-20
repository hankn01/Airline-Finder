import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime

#라이브러리 import

form_class = uic.loadUiType("메인 화면.ui")[0]
#Qt UI와 연동
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.CloseButton.clicked.connect(self.CLSBTN)
        
    def initUI(self):
        #출발지 목록 추가
        self.FromCmb.addItem('출발지를 선택하여 주세요')
        self.FromCmb.addItem('서울/김포(GMP)')
        self.FromCmb.addItem('부산/김해(PUS)')
        self.FromCmb.addItem('제주(CJU)')
        self.FromCmb.addItem('대구(TAE)')
        self.FromCmb.addItem('무안(MWX)')
        self.FromCmb.addItem('양양(YNY)')
        self.FromCmb.addItem('청주(CJJ)')
        self.FromCmb.addItem('원주(WNJ)')
        self.FromCmb.addItem('군산(KUV)')
        self.FromCmb.addItem('광주(KWJ)')
        self.FromCmb.addItem('여수(RSU)')
        self.FromCmb.addItem('포항(KPO)')
        self.FromCmb.addItem('울산(USN)')
        self.FromCmb.addItem('진주/사천(HIN)')
        #도착지 목록 추가
        self.ToCmb.addItem('도착지를 선택하여 주세요')
        self.ToCmb.addItem('서울/김포(GMP)')
        self.ToCmb.addItem('부산/김해(PUS)')
        self.ToCmb.addItem('제주(CJU)')
        self.ToCmb.addItem('대구(TAE)')
        self.ToCmb.addItem('무안(MWX)')
        self.ToCmb.addItem('양양(YNY)')
        self.ToCmb.addItem('청주(CJJ)')
        self.ToCmb.addItem('원주(WNJ)')
        self.ToCmb.addItem('군산(KUV)')
        self.ToCmb.addItem('광주(KWJ)')
        self.ToCmb.addItem('여수(RSU)')
        self.ToCmb.addItem('포항(KPO)')
        self.ToCmb.addItem('울산(USN)')
        self.ToCmb.addItem('진주/사천(HIN)')
	
        self.Company.addItem('KE')
        self.Company.addItem('OZ')
        self.Company.addItem('BX')
        self.Company.addItem('7C')
        self.Company.addItem('LJ')
        self.Company.addItem('TW')
        self.Company.addItem('RS')
        self.Company.addItem('ALL')
	
        self.Language.addItem('한국어/Korean')
        self.Language.addItem('English')
        self.Language.addItem('日本語/Japanese')
        self.Language.addItem('中文/Chinese')
        self.Language.addItem('Español/Spanish')
        for i in range(datetime.today().year, datetime.today().year+3) :
            self.YearCmb.addItem(str(i))
        for j in range(1,13) :
            self.MonthCmb.addItem(str(j))
        #날짜의 경우 월에 따라 28, 30, 31일로 분기 처리
        for k in range(1, 32) :
            self.DateCmb.addItem(str(k))
        
        #선택된 날짜에 따라 if문으로 분기

    def CLSBTN(self):
        exit();

#윈도우 실행 함수
if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
    

    
