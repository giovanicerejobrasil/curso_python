"""
QWidget e QLayout de PySide6.QtWidgets
QWidget -> genérico
QLayout -> Um widget de layout que recebe outros widgets
"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)
central_widget = QWidget()
layout = QGridLayout()

button = QPushButton('Botão 1')
button.setStyleSheet('font-size: 40px; color: red;')

button_2 = QPushButton('Botão 2')
button_2.setStyleSheet('font-size: 40px; color: green;')

button_3 = QPushButton('Botão 3')
button_3.setStyleSheet('font-size: 40px; color: blue;')

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button_2, 1, 2, 1, 1)
layout.addWidget(button_3, 2, 1, 1, 2)

central_widget.setLayout(layout)
central_widget.show()

app.exec()  # Loop da aplicação
