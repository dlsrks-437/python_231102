import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans


form_class = uic.loadUiType('UI/googleTransUI.ui')[0]
#  QTdesigner에서 제작한 UI 불러오기

class GoogleTranslate(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 초기화자 호출
        self.setupUi(self)  # 제작해놓은 UI 연결
        self.setWindowTitle('구글 번역기')  # 번역기 앱 타이틀
        self.setWindowIcon(QIcon('D:/KimHyunJae/자료/아이콘/google_icon.png'))  # 앱 아이콘
        self.statusBar().showMessage('Google Transe App v1.0_Copyright ⓒ by dlsrks-437')

        self.btn_trans.clicked.connect(self.trans_function)
        self.reset_btn.clicked.connect(self.reset)

    def trans_function(self):
        trans_kor = self.input_kor_text.text()  # input_kor_text에 입력된 한글 가져오기

        # print(googletrans.LANGUAGES)  # 번역 언어 tricker 불러오기

        trans = googletrans.Translator()  # 구글 트랜스 모듈의 객체(번역기)
        trans_eng = trans.translate(trans_kor, dest='en')
        trans_jpn = trans.translate(trans_kor, dest='ja')
        trans_chi = trans.translate(trans_kor, dest='zh-cn')

        self.output_eng_text.append(trans_eng.text)
        self.output_jap_text.append(trans_jpn.text)
        self.output_chn_text.append(trans_chi.text)

    def reset(self):
        self.input_kor_text.clear()
        self.output_eng_text.clear()
        self.output_jap_text.clear()
        self.output_chn_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = GoogleTranslate()
    myApp.show()
    sys.exit(app.exec_())












