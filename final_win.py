from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # comprobar los tipos de los valores de entrada
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
   def __init__(self, exp):
       ''' la ventana en donde se realizan las preguntas '''
       super().__init__()

       # obteniendo los datos sobre el experimento
       self.exp = exp

       # creando y configurando elementos gráficos
       self.initUI()

       # establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
       self.set_appear()
      
       # inicio:
       self.show()


   def results(self):
       if self.exp.age < 7:
           self.index = 0
           return "no hay datos para esta edad"
       
       # CORRECCIÓN: Se cambiaron t1, t2 y t3 por test1, test2 y test3
       self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10
       
       if self.exp.age == 7 or self.exp.age == 8:
           if self.index >= 21:
               return txt_res1
           elif self.index < 21 and self.index >= 17:
               return txt_res2
           elif self.index < 17 and self.index >= 12:
               return txt_res3
           elif self.index < 12 and self.index >= 6.5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 9 or self.exp.age == 10:
           if self.index >= 19.5:
               return txt_res1
           elif self.index < 19.5 and self.index >= 15.5:
               return txt_res2
           elif self.index < 15.5 and self.index >= 10.5:
               return txt_res3
           elif self.index < 10.5 and self.index >= 5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 11 or self.exp.age == 12:
           if self.index >= 18:
               return txt_res1
           elif self.index < 18 and self.index >= 14:
               return txt_res2
           elif self.index < 14 and self.index >= 9:
               return txt_res3
           elif self.index < 9 and self.index >= 3.5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 13 or self.exp.age == 14:
           if self.index >= 16.5:
               return txt_res1
           elif self.index < 16.5 and self.index >= 12.5:
               return txt_res2
           elif self.index < 12.5 and self.index >= 7.5:
               return txt_res3
           elif self.index < 7.5 and self.index >= 2:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age >= 15:
           if self.index >= 15:
               return txt_res1
           elif self.index < 15 and self.index >= 11:
               return txt_res2
           elif self.index < 11 and self.index >= 6:
               return txt_res3
           elif self.index < 6 and self.index >= 0.5:
               return txt_res4
           else:
               return txt_res5


   def initUI(self):
       ''' crea elementos gráficos '''
       # Llamamos a results primero para asegurarnos de que calcule self.index antes de usarlo abajo
       resultado_texto = self.results() 
       
       self.work_text = QLabel(txt_workheart + resultado_texto)
       self.index_text = QLabel(txt_index + str(self.index))

       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout_line)


   def set_appear(self):
       ''' establece la apariencia de la ventana (etiqueta, tamaño, ubicación) '''
       self.setWindowTitle(txt_finalwin)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)