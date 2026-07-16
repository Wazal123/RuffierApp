from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont 
from PyQt5.QtWidgets import (
       QWidget, QHBoxLayout, QVBoxLayout, 
       QPushButton, QLabel, QLineEdit)

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        # Nombres corregidos para que final_win.py no lance AttributeError
        self.test1 = test1  
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        ''' La ventana en donde se realizan las preguntas y pruebas '''
        super().__init__()

        # Creando y configurando elementos gráficos
        self.initUI()

        # Establece la conexión entre los elementos (eventos)
        self.connects()

        # Establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
        self.set_appear()
       
        # Inicio de la ventana:
        self.show()

    def set_appear(self):
        ''' Establece el título, tamaño y posición de la ventana usando las variables de instr.py '''
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        ''' Crea y distribuye todos los elementos gráficos en la pantalla '''
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        # Contenedores (Layouts)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        # Panel Derecho: Cronómetro
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)

        # Panel Izquierdo: Formulario estructurado secuencialmente
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        
        self.l_line.addWidget(self.text_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment=Qt.AlignLeft)
        
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)
        
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        # Integración de layouts
        self.h_line.addLayout(self.l_line) 
        self.h_line.addLayout(self.r_line)       
        self.setLayout(self.h_line)

    def next_click(self):
        ''' Procesa los datos, los empaqueta en Experiment y cambia a la ventana final '''
        try:
            # Evita crasheos si el usuario no pone números en la edad
            edad = int(self.line_age.text()) if self.line_age.text() else 0
        except ValueError:
            edad = 0

        # Corrección de la duplicación: tomamos de forma única cada caja de texto
        t1 = self.line_test1.text()
        t2 = self.line_test2.text()
        t3 = self.line_test3.text()

        self.hide()
        
        # Se genera el objeto con la estructura que final_win.py espera
        self.exp = Experiment(edad, t1, t2, t3)
        self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        # Una sentadilla cada 1.5 segundos (30 sentadillas en 45 segundos reales)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        
        # Control visual de colores según las fases del test final de Ruffier-Dickson
        segundos = int(time.toString("hh:mm:ss")[6:8])
        if segundos >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")  # Verde (Primeros 15s)
        elif segundos <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")  # Verde (Últimos 15s)
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")    # Negro (Descanso intermedio)
            
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        ''' Vincula los clics de los botones a sus respectivas funciones ejecutables '''
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)