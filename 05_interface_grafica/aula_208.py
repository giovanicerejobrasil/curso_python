"""
O básico sobre Signal e Slots (eventos e documentação)
"""
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QPushButton, QWidget, QMainWindow,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()

button_1 = QPushButton('Botão 1')
button_1.setStyleSheet('font-size: 30px; color: red')

button_2 = QPushButton('Botão 2')
button_2.setStyleSheet('font-size: 30px; color: green')

button_3 = QPushButton('Botão 3')
button_3.setStyleSheet('font-size: 30px; color: blue')

layout.addWidget(button_1, 1, 1, 1, 1)
layout.addWidget(button_2, 1, 2, 1, 1)
layout.addWidget(button_3, 2, 1, 1, 2)

central_widget.setLayout(layout)

window.setWindowTitle('Meu título')
window.resize(300, 200)
window.setCentralWidget(central_widget)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('Mudando a mensagem da status bar')
    return inner


@Slot()
def other_slot(is_checked):
    print("Checked:", is_checked)


@Slot()
def third_slot(action):
    def inner():
        print("Checked:", action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Minha barra de status')

# menuBar
menu_bar = window.menuBar()

first_menu = menu_bar.addMenu('Primeiro Menu')

first_action = first_menu.addAction('Primeira Ação')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Segunda Ação')
second_action.setCheckable(True)
second_action.toggled.connect(other_slot)
second_action.hovered.connect(third_slot(second_action))

button_3.clicked.connect(third_slot(second_action))

window.show()

app.exec()
