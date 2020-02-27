# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:50:25 2020


# 디자이너: C:\Programs\Anaconda3\Library\bin\designer.exe 
# 스파이더에서는 한번 실행하면 프로세스가 죽음

@author: 20605019
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 화면 UI파일
form_class = uic.loadUiType("main_window.ui")[0]

# 사용자UI 클래스 생성 : QMainWindow 상속, ui form 전달
class MyWindow(QMainWindow, form_class):

    # 생성자
    def __init__(self):
        # setupUi() 호출하여 UI 구성
        super().__init__()
        self.setupUi(self)
        plt.rcParams["font.family"] = 'Malgun Gothic'

        # 버튼에 이벤트 함수 연결
        self.btnOk.clicked.connect(self.btn_clicked)
        self.chkExclude.clicked.connect(self.chk_clicked)
        
        # 데이터 로딩
        self.loadMemberList()
        self.loadChart()


    # 버튼 이벤트 함수 정의
    def btn_clicked(self):
        self.txtName.setText("Msg")
        QMessageBox.about(self, "체크박스", str(self.chkExclude.isChecked()))


    # 위젯 이벤트 함수 정의
    def chk_clicked(self):
        QMessageBox.about(self, "message", "clicked")


    # 테이블 로딩 함수
    def loadMemberList(self):
        data = [['20601001', '홍길동', '매니저', '총무팀'],
                ['20501009', '이순신', '책임', '인사팀']]
        df = pd.DataFrame(data, columns=['사번', '이름', '직급', '부서'])

        self.tblMemberList.setRowCount(len(df))
        
        for i, r in df.iterrows():
            r.index = range(0, len(r))
            for j, v in r.iteritems():
                self.tblMemberList.setItem(i, j, QTableWidgetItem(v))

        self.tblMemberList.resizeColumnsToContents()
    
    # 챠트 로딩 함수
    def loadChart(self):
        data = {'Name' : ['홍길동', '이순신', '강감찬', '유관순'],
                'Point': [60, 80, 70, 50]}
        df = pd.DataFrame(data, index=data['Name'])
        
        ax = df.plot.bar(figsize=(8, 3))
        canvas = FigureCanvas(ax.figure)
        canvas.draw()
        self.wgtChart.addWidget(canvas)
        


# 메인함수
if __name__ == "__main__":
    # 사용자Ui 클래스 생성 및 메세지 루프 실행
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

