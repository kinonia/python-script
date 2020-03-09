# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:51:01 2020

@author: 20605019
"""

import sys
import socket
import datetime as dt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from PyQt5 import uic

# 화면 UI파일
form_class = uic.loadUiType("server_window.ui")[0]

# 사용자UI 클래스 생성 : QMainWindow 상속, ui form 전달
class MyWindow(QMainWindow, form_class):

    # 생성자
    def __init__(self):
        # setupUi() 호출하여 UI 구성
        super().__init__()
        self.setupUi(self)

        # 송/수신간 이벤트 핸들러 연결(2)
        self._commmunicate = Communicate(self)
        #self._commmunicate.receivedMessage.connect(self.com_received_message)
        self._commmunicate.start()


    # 이벤트 함수 -------------------------------------------------------------
    # 수신자 : receiver, 슬롯/이벤트 핸들러 처리, 사용자가 정의함
    #@pyqtSlot(str)
    def com_received_message(self, msg):
        #QMessageBox.about(self, "message", msg)
        self.txtName.setText(msg)
        
        i = self.tblLogs.rowCount() + 1
        self.tblLogs.setRowCount(i)
        self.tblLogs.setItem(i - 1, 0, QTableWidgetItem(str(dt.datetime.today())))
        self.tblLogs.setItem(i - 1, 1, QTableWidgetItem(msg))
        self.tblLogs.resizeColumnsToContents()



# 서버통신 클래스 -----------------------------------------------------------------
class Communicate(QThread):
    # 송신자 : sender, 시그널/이벤트 생성, clicked/valueChanged
    #receivedMessage = pyqtSignal(str)
    
    # 생성자
    def __init__(self, parents):
        super().__init__()
        self._parents = parents
        
        self._server = socket.socket()
        self._server.bind(('localhost', 8888))
        self._server.listen(1)      # 클라이언트 1대만 접속


    # 시작함수
    def run(self):
        #QThread.sleep(3)
        
        # 직접호출 코드(1)
        #self._parents.com_received_message("나와라 성공?")
        
        # 이벤트 핸들러 통해 호출 코드(2)
        #self.receivedMessage.emit("간접 나와라.")
        
        while True:
            # 클라이언트 접속
            conn, address = self._server.accept()
            self._parents.com_received_message(f"클라이언트 접속: {str(address)}")
            
            # 클라이언트 메시지 처리
            while True:
                recv = conn.recv(1024).decode().strip()     # 1024byte 이내만 읽기
                self._parents.com_received_message(f'수신:{recv}')
                
                resp = f'회신:{recv}'
                conn.send(resp.encode())
                self._parents.com_received_message(f'{resp}')
                
                if not recv:
                    break
                elif recv.startswith('Q'):
                    break
            
            conn.close()
            self._parents.com_received_message(f"클라이언트 종료:{str(address)}")
    
    

# 메인함수 --------------------------------------------------------------------
if __name__ == "__main__":
    # 사용자Ui 클래스 생성 및 메세지 루프 실행
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

