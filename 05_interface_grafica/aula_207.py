"""
QMainWindow e centralWidget
-> QApplication (app)
  -> QMainWindow (window->setCentralWidget)
      -> CentralWidget (central_widget)
          -> Layout (layout)
              -> Widget 1 (botao1)
              -> Widget 2 (botao2)
              -> Widget 3 (botao3)
  -> show
-> exec
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QPushButton, QWidget, QMainWindow
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


def slot_example(status_bar) -> None:
    status_bar.showMessage('Mudando a mensagem da status bar')


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Minha barra de status')

# menuBar
menu_bar = window.menuBar()

first_menu = menu_bar.addMenu('Primeiro Menu')

first_action = first_menu.addAction('Primeira Ação')
first_action.triggered.connect(
    lambda: slot_example(status_bar)
)

window.show()

app.exec()
