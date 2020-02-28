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
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 화면 UI파일
form_class = uic.loadUiType("basic_window.ui")[0]

# 사용자UI 클래스 생성 : QMainWindow 상속, ui form 전달
class MyWindow(QMainWindow, form_class):

    # 생성자
    def __init__(self):
        # setupUi() 호출하여 UI 구성
        super().__init__()
        self.setupUi(self)
        
        # 추가 화면 구성
        plt.rcParams["font.family"] = 'Malgun Gothic'
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.wgtChart.addWidget(self.canvas)
        
        # 버튼에 이벤트 함수 연결
        # 송신자 : sender, 시그널/이벤트 생성, clicked/valueChanged
        # 수신자 : receiver, 슬롯/이벤트 핸들러 처리, 사용자가 정의함
        self.chkExclude.clicked.connect(self.chk_clicked)
        self.btnTable.clicked.connect(self.btn_table_clicked)
        self.btnChart.clicked.connect(self.btn_chart_clicked)
        self.btnImage.clicked.connect(self.btn_image_clicked)


    # 이벤트 함수 -------------------------------------------------------------
    # 위젯 이벤트 처리 함수 정의
    def chk_clicked(self):
        self.txtName.setText("Msg")
        QMessageBox.about(self, "message", str(self.chkExclude.isChecked()))


    # 테이블 버튼 이벤트 처리 함수 정의
    def btn_table_clicked(self):
        QMessageBox.about(self, "로딩", "테이블시작")
        self.loadMemberList()


    # 챠트 버튼 이벤트 처리 함수 정의
    def btn_chart_clicked(self):
        QMessageBox.about(self, "로딩", "챠트시작")
        self.loadChart()


    # 이미지 버튼 이벤트 처리 함수 정의
    def btn_image_clicked(self):
        srcImage = QFileDialog.getOpenFileName(self)[0]
        self.loadImage(srcImage)


    # 사용자 함수 -------------------------------------------------------------
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
        
        # ax = df.plot.bar(figsize=(8, 3))
        # canvas = FigureCanvas(ax.figure)
        # canvas.draw()
        # self.wgtChart.addWidget(canvas)

        ax1 = self.fig.add_subplot(111)
        df.plot.bar(ax=ax1)
        self.canvas.draw()


    # 이미지 로딩 함수
    def loadImage(self, srcImage):
        image_data = QImage()
        image_data.load(srcImage)

        image = QPixmap()
        image = QPixmap.fromImage(image_data)
        image = image.scaledToWidth(500)#, Qt.IgnoreAspectRatio)

        scene = QGraphicsScene()
        scene.addPixmap(image)
        
        # QGraphicsView를 UI에 구성한 뒤 추가
        # self.picImage.setScene(scene)
        # print(type(self.picImage))

        pic = QGraphicsView()
        pic.setScene(scene)
        self.wgtChart.addWidget(pic)



# 메인함수 --------------------------------------------------------------------
if __name__ == "__main__":
    # 사용자Ui 클래스 생성 및 메세지 루프 실행
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

