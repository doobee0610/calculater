# calculator.py
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QPushButton)
from PyQt5.QtCore import Qt

# 메인 윈도우 클래스 정의, QMainWindow를 상속받음
class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. 기본 창 설정
        self.setWindowTitle('계산기')  # 창 제목 설정
        self.setGeometry(300, 300, 400, 500)  # 창 위치(x, y)와 크기(너비, 높이) 설정

        # 중앙 위젯 및 전체 레이아웃 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 3. 레이아웃: 전체적인 구조는 수직 레이아웃(QVBoxLayout) 사용
        vbox = QVBoxLayout()
        central_widget.setLayout(vbox)

        # 2. 화면 구성 요소 (위젯)
        # 디스플레이 화면 (QTextEdit) 생성
        self.display = QTextEdit()
        self.display.setReadOnly(True)  # 읽기 전용으로 설정하여 사용자 입력 방지
        self.display.setStyleSheet("font-size: 20px;") # 폰트 크기 설정

        # 버튼 그룹을 담을 위젯과 수평 레이아웃(QHBoxLayout) 생성
        button_widget = QWidget()
        hbox = QHBoxLayout()
        button_widget.setLayout(hbox)

        # '메시지' 버튼 생성
        self.message_button = QPushButton('메시지')
        
        # 'clear' 버튼 생성
        self.clear_button = QPushButton('clear')

        # 수평 레이아웃에 버튼 추가
        hbox.addWidget(self.message_button)
        hbox.addWidget(self.clear_button)

        # 수직 레이아웃에 디스플레이와 버튼 그룹 추가
        vbox.addWidget(self.display)
        vbox.addWidget(button_widget)

        # 4. 기능 및 동작 연결
        # '메시지' 버튼 클릭 시 on_message_button_clicked 함수 호출
        self.message_button.clicked.connect(self.on_message_button_clicked)
        
        # 'clear' 버튼 클릭 시 on_clear_button_clicked 함수 호출
        self.clear_button.clicked.connect(self.on_clear_button_clicked)

    def on_message_button_clicked(self):
        """'메시지' 버튼 클릭 시 호출되는 함수"""
        # 디스플레이 화면에 'Button Clicked' 텍스트를 한 줄씩 추가
        self.display.append('Button Clicked')

    def on_clear_button_clicked(self):
        """'clear' 버튼 클릭 시 호출되는 함수"""
        # 디스플레이 화면의 모든 텍스트를 지움
        self.display.clear()

# 5. 코드 구조: 스크립트 직접 실행 시 프로그램 시작
if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)
    
    # CalculatorApp 인스턴스 생성
    ex = CalculatorApp()
    
    # 창을 화면에 보여줌
    ex.show()
    
    # 애플리케이션 이벤트 루프 실행
    sys.exit(app.exec_())
