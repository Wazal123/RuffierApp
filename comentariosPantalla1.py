# Importación de constantes de alineación y controles (widgets) desde PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, 
    QLabel, QPushButton, QLineEdit,
    QRadioButton, QGroupBox, QListWidget)

# Importación de textos/variables externas (títulos, instrucciones, etc.)
from instr import *
# Importación de la segunda ventana (TestWin) para poder abrirla después
from second_win import *

# Definición de la clase para la ventana principal, que hereda de QWidget
class MainWin(QWidget):
    def __init__(self):
        '''primera pantalla'''
        super().__init__() # Inicializa la clase padre (QWidget)

        self.initUI()      # Crea y organiza los elementos visuales (botones, textos)

        self.connects()    # Conecta los eventos (por ejemplo, clics en botones) con sus funciones

        self.set_appear()  # Configura el tamaño, título y posición de la ventana

        self.show()        # Hace que la ventana sea visible en la pantalla

    def initUI(self):
        """Crea los componentes visuales y los organiza en el diseño (layout)"""
        # Creación de los elementos: botón y etiquetas de texto
        self.btn_netx = QPushButton(txt_next, self)  # Nota: hay un pequeño typo en 'netx', pero funciona igual
        self.hello_text = QLabel(txt_hello)
        self.instruccion = QLabel(txt_instruction)

        # Creación de un diseño vertical para alinear los elementos uno abajo del otro
        self.layout_line = QVBoxLayout()
        
        # Añadir los elementos al diseño con sus respectivas alineaciones
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)   # Texto de bienvenida a la izquierda
        self.layout_line.addWidget(self.instruccion, alignment = Qt.AlignLeft)  # Instrucciones a la izquierda
        self.layout_line.addWidget(self.btn_netx, alignment = Qt.AlignCenter)   # Botón centrado
        
        # Establecer este diseño vertical como el principal de la ventana
        self.setLayout(self.layout_line)
    
    def next_click(self):
        """Función que se ejecuta al hacer clic en el botón Siguiente"""
        self.TW = TestWin() # Instancia (crea) la segunda ventana
        self.hide()         # Oculta la ventana actual (la primera pantalla)

    def connects(self):
        """Establece las conexiones entre las acciones del usuario y el código"""
        # Al hacer clic en el botón, se llama al método 'next_click'
        self.btn_netx.clicked.connect(self.next_click)

    def set_appear(self):
        """Define las propiedades estéticas y de ubicación de la ventana"""
        self.setWindowTitle(txt_title)         # Define el título de la ventana
        self.resize(win_width, win_height)     # Cambia el tamaño (ancho, alto)
        self.move(win_x, win_y)                 # Mueve la ventana a las coordenadas X e Y de la pantalla

# --- Flujo principal del programa ---

# 1. Crea la aplicación base necesaria para que PyQt funcione
app = QApplication([])

# 2. Crea la instancia de nuestra ventana principal (lo que dispara el __init__)
mw = MainWin()

# 3. Inicia el bucle de eventos de la aplicación (mantiene el programa abierto hasta que lo cierres)
app.exec_()