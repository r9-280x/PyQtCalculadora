from PyQt6.QtWidgets import QApplication, QFormLayout, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QWidget, QMainWindow
from PyQt6.QtGui import QKeySequence, QFont

import sys
from PyQt6.QtCore import Qt

class Ventana_principal(QWidget):
    def __init__(self):
        super().__init__()
        self.generar_ui()

    def generar_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.setWindowTitle("Calculadora")
        self.generar_formulario()
    
    def generar_formulario(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        self.pantalla.setFixedHeight(100)
        self.pantalla.setFixedWidth(380)


        # Modificar las fuentes
        fuente_buttons = QFont("Segoe UI", 15)
        fuente_pantalla = QFont("Segoe UI Bold", 15)

        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")
        # Operaciones de la calculadora
        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("×")
        boton_division = QPushButton("÷")
        
        boton_ce = QPushButton("CE")
        boton_borrar = QPushButton("←")
        boton_resultado = QPushButton("=")

        botones = [boton_0, boton_1, boton_2, boton_3, boton_4, boton_5, boton_6, boton_7,boton_8, boton_9, boton_00, boton_punto, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_ce, boton_borrar, boton_resultado]

        for boton in botones:
            boton.setFont(fuente_buttons)

        
        self.pantalla.setFont(fuente_pantalla)

        # Tamaño de los botones

        boton_1.setFixedSize(85, 65)
        boton_2.setFixedSize(85, 65)
        boton_3.setFixedSize(85, 65)
        boton_4.setFixedSize(85, 65)
        boton_5.setFixedSize(85, 65)
        boton_6.setFixedSize(85, 65)
        boton_7.setFixedSize(85, 65)
        boton_8.setFixedSize(85, 65)
        boton_9.setFixedSize(85, 65)
        boton_0.setFixedSize(85, 65)
        boton_00.setFixedSize(85, 65)
        boton_punto.setFixedSize(85, 65)
        boton_suma.setFixedSize(85, 65)
        boton_resta.setFixedSize(85, 65)
        boton_multiplicacion.setFixedSize(85, 65)
        boton_division.setFixedSize(85, 65)
        boton_ce.setFixedSize(185, 65)
        boton_borrar.setFixedSize(85, 65)
        boton_resultado.setFixedSize(85, 65)

        self.grid_principal = QGridLayout()
        self.grid_principal.addWidget(self.pantalla, 0, 0, 2, 4)
        self.grid_principal.addWidget(boton_ce, 2, 0, 1, 2)
        self.grid_principal.addWidget(boton_borrar, 2, 2)
        self.grid_principal.addWidget(boton_suma, 2, 3)
        self.grid_principal.addWidget(boton_7, 3,0)
        self.grid_principal.addWidget(boton_8, 3,1)
        self.grid_principal.addWidget(boton_9, 3,2)
        self.grid_principal.addWidget(boton_division, 3,3)
        
        self.grid_principal.addWidget(boton_6, 4,0)
        self.grid_principal.addWidget(boton_5, 4,1)
        self.grid_principal.addWidget(boton_4, 4,2)
        self.grid_principal.addWidget(boton_multiplicacion, 4,3)

        self.grid_principal.addWidget(boton_1, 5,0)
        self.grid_principal.addWidget(boton_2, 5,1)
        self.grid_principal.addWidget(boton_3, 5,2)
        self.grid_principal.addWidget(boton_resta, 5,3)
        
        self.grid_principal.addWidget(boton_0, 6,0)
        self.grid_principal.addWidget(boton_00, 6,1)
        self.grid_principal.addWidget(boton_punto, 6,2)
        self.grid_principal.addWidget(boton_resultado, 6,3)
        self.setLayout(self.grid_principal)

         # Conectar los botones con sus funciones
        boton_1.clicked.connect(lambda: self.agregar_a_pantalla("1"))
        boton_2.clicked.connect(lambda: self.agregar_a_pantalla("2"))
        boton_3.clicked.connect(lambda: self.agregar_a_pantalla("3"))
        boton_4.clicked.connect(lambda: self.agregar_a_pantalla("4"))
        boton_5.clicked.connect(lambda: self.agregar_a_pantalla("5"))
        boton_6.clicked.connect(lambda: self.agregar_a_pantalla("6"))
        boton_7.clicked.connect(lambda: self.agregar_a_pantalla("7"))
        boton_8.clicked.connect(lambda: self.agregar_a_pantalla("8"))
        boton_9.clicked.connect(lambda: self.agregar_a_pantalla("9"))
        boton_0.clicked.connect(lambda: self.agregar_a_pantalla("0"))
        boton_00.clicked.connect(lambda: self.agregar_a_pantalla("00"))
        boton_punto.clicked.connect(lambda: self.agregar_a_pantalla("."))
        boton_suma.clicked.connect(lambda: self.agregar_a_pantalla("+"))
        boton_resta.clicked.connect(lambda: self.agregar_a_pantalla("-"))
        boton_multiplicacion.clicked.connect(lambda: self.agregar_a_pantalla("×"))
        boton_division.clicked.connect(lambda: self.agregar_a_pantalla("÷"))
        boton_ce.clicked.connect(lambda: self.limpiar_pantalla())
        boton_resultado.clicked.connect(lambda: self.calcular_resultado())
        boton_borrar.clicked.connect(lambda: self.borrar_ultimo_caracter())


    def agregar_a_pantalla(self, texto):
    # Agregar texto a la pantalla (QTextEdit).
        current_text = self.pantalla.toPlainText()  # Obtiene el texto actual que se muestra en la pantalla
        self.pantalla.setPlainText(current_text + texto)  # Agrega el nuevo texto al final del texto actual
    

    # Capturar las teclas presionadas

    def keyPressEvent(self, tecla):
        key = tecla.key()

        # Numeros

        if key == Qt.Key.Key_1: self.agregar_a_pantalla("1")
        elif key == Qt.Key.Key_2: self.agregar_a_pantalla("2")
        elif key == Qt.Key.Key_3: self.agregar_a_pantalla("3")
        elif key == Qt.Key.Key_4: self.agregar_a_pantalla("4")
        elif key == Qt.Key.Key_5: self.agregar_a_pantalla("5")
        elif key == Qt.Key.Key_6: self.agregar_a_pantalla("6")
        elif key == Qt.Key.Key_7: self.agregar_a_pantalla("7")
        elif key == Qt.Key.Key_8: self.agregar_a_pantalla("8")
        elif key == Qt.Key.Key_9: self.agregar_a_pantalla("9")
        elif key == Qt.Key.Key_0: self.agregar_a_pantalla("0")
    # Operadores
        elif key == Qt.Key.Key_Plus: self.agregar_a_pantalla("+")
        elif key == Qt.Key.Key_Minus: self.agregar_a_pantalla("-")
        elif key == Qt.Key.Key_Asterisk: self.agregar_a_pantalla("×")  # Multiplicación
        elif key == Qt.Key.Key_Slash: self.agregar_a_pantalla("÷")  # División
        
        # Tecla de borrar
        elif key == Qt.Key.Key_Backspace: self.borrar_ultimo_caracter()

        # Tecla de punto
        elif key == Qt.Key.Key_Period: self.agregar_a_pantalla(".")

        # Tecla Enter (o igual)
        elif key == Qt.Key.Key_Enter or key == Qt.Key.Key_Return:
            self.calcular_resultado()

        # Tecla CE para limpiar la pantalla
        elif key == Qt.Key.Key_Escape:
            self.limpiar_pantalla()

        tecla.accept()  # Aceptar el evento

    def agregar_a_pantalla(self, texto):
        """Agregar texto a la pantalla (QTextEdit)."""
        current_text = self.pantalla.toPlainText()
        self.pantalla.setPlainText(current_text + texto)

    def calcular_resultado(self):
        """Evaluar la expresión matemática y mostrar el resultado."""
        try:
            # Obtener el texto de la pantalla de la calculadora
            expression = self.pantalla.toPlainText()
            # Reemplazar los simbolos de operacion correspondientes
            expression = expression.replace("×", "*").replace("÷", "/")
            result = eval(expression)   # Evaluar la expresion
            formatted_result = f"{result:,}"
            self.pantalla.setPlainText(str(formatted_result)) # Mostrar el resultado en pantalla
        except Exception:
            # Si ocurre algun error, mostrar en pantalla
            self.pantalla.setPlainText("Syntax Error")

    def limpiar_pantalla(self):
        """Limpiar la pantalla."""
        self.pantalla.clear()

    def borrar_ultimo_caracter(self):
        """Eliminar el último carácter de la pantalla."""
        current_text = self.pantalla.toPlainText()
        if current_text: # Eliminar solo si hay texto en pantalla
            new_text = current_text[:-1]    # Eliminar el ultimo caracter
            self.pantalla.setPlainText(new_text) # Actualizar pantalla

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ventana_principal()
    ui.show()
    sys.exit(app.exec())