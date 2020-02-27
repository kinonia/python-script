# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:16:58 2020

@author: 20605019
"""

# #############################################################################
# 클래스 정의
class Card:
    def print_info(self):
        pass

# 클래스 상속 : 클래스명 뒤에 상속받을 클래스 기입
class BusinessCard(Card):
    
    # 클래스 변수 : 클래스이름.으로 사용함, 모든 인스턴스 공용 변수
    num_business_card = 0
    
    # 생성자
    def __init__(self, name, email, addr):
        # 인스턴스 변수 : self.과 같이 앞에 붙여서 구분함
        self.name = name
        self.email = email
        self.addr = addr
    
    # 클래스 메서드 : 첫번째 인자는 반드시 self로 고정
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
        
        # 함수호출1: self.으로 호출, 첫인자에 self 넣지 않음
        self.print_info()
    
    # 클래스 메서드
    def print_info(self):
        print("--------------------")
        print("Name: ",     self.name)
        print("E-mail: ",   self.email)
        print("Address: ",  self.addr)
        print("--------------------")
    
    # 함수: self 인자가 없어서 호출불가
    def test():
        print("xxx")


# #############################################################################
# 프로그램 시작 처리
if __name__ == "__main__":
    
    # 객체 생성
    bc = BusinessCard("Kangsan Lee", "kangsan.lee", "USA")
    
    # 함수 호츨2: 변수명.으로 호출, 첫인자에 self 넣지 않음
    bc.print_info()
    BusinessCard.print_info(bc)
    
    # 함수: self 인자가 없어서 호출불가
    #bc.test(bc)
    
    # 클래스 내장속성
    print(bc.__dict__)
    
    

