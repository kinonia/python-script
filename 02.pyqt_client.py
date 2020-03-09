# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:51:05 2020

@author: 20605019
"""


import sys
import socket
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면 UI파일
form_class = uic.loadUiType("client_window.ui")[0]

# 사용자UI 클래스 생성 : QMainWindow 상속, ui form 전달
class MyWindow(QMainWindow, form_class):

    # 생성자
    def __init__(self):
        # setupUi() 호출하여 UI 구성
        super().__init__()
        self.setupUi(self)
        
        self.btnSend.clicked.connect(self.btn_send_clicked)
        
        # 클라이언트 소켓으로 서버연결
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(('localhost', 8888))


    # 전송 버튼 클릭
    def btn_send_clicked(self):
        print("send:" + self.txtSend.text())
        
        # 메시지를 전송합니다. 
        self._client.sendall(self.txtSend.text().encode())

        # 메시지를 수신합니다. 
        data = self._client.recv(1024)
        self.txtRec.setText( repr(data.decode()) )



# 메인함수 --------------------------------------------------------------------
if __name__ == "__main__":
    # 사용자Ui 클래스 생성 및 메세지 루프 실행
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
