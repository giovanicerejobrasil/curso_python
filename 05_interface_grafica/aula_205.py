"""
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação

QPushButton -> Um botão

PySide6.QtWidgets -> Onde estão os widgets do PySide6
"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Botão 1')
button.setStyleSheet('font-size: 40px; color: red;')
button.show()  # Adiciona o botão na hierarquia e exibe a janela

button_2 = QPushButton('Botão 2')
button_2.setStyleSheet('font-size: 40px; color: blue;')
button_2.show()

app.exec()  # Loop da aplicação
