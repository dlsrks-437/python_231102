import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans


from_class = uic.loadUiType('UI/googleTransUI.ui')[0]
#  QTdesigner에서 제작한 UI 불러오기

class GoogleTranslate(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 초기화자 호출
        self.setupUi(self)  # 제작해놓은 UI 연결
        self.setWindowTitle('구글 번역기')  # 번역기 앱 타이틀
        self.setWindowIcon(QIcon('D:\KimHyunJae\자료\아이콘\google_icon.png'))  # 앱 아이콘
        self.statusBar().showMessage('Google Transe App v1.0_Copyright by dlsrks-437')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = GoogleTranslate()
    myApp.show()
    sys.exit(app.exec_())












