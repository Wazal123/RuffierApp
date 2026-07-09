from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, 
    QLabel, QPushButton, QLineEdit,
    QRadioButton, QGroupBox, QListWidget)


from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        '''primera pantalla'''
        super().__init__()

        self.initUI()

        self.connects()

        self.set_appear()

        self.show()

    def initUI(self):
    
        self.btn_netx = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruccion = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruccion, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_netx, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    
    def next_click(self):
        self.TW = TestWin()
        self.hide()

    def connects(self):
        self.btn_netx.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()

