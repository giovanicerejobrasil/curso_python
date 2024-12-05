"""
Trabalhando com classes e herança no PySide6
"""
import sys
import re
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QPushButton, QWidget, QMainWindow,
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Central Widget
        self.central_widget = QWidget()

        # Grid Layout
        self.grid_layout = QGridLayout()

        # Button 1
        self.button_1 = self.make_button(
            'Botão 1',
            {
                'font-size': '30px',
                'color': 'red',
                'background-color': 'lightgray'
            }
        )
        self.button_1.clicked.connect(self.second_action_checked)

        # Button 2
        self.button_2 = self.make_button(
            'Botão 2',
            {
                'font-size': '30px',
                'color': 'green',
                'background-color': 'violet'
            }
        )

        # Button 3
        self.button_3 = self.make_button(
            'Botão 3',
            {
                'font-size': '30px',
                'color': 'blue',
                'background-color': 'darkkhaki'
            }
        )
        self.button_3.clicked.connect(self.second_action_checked)

        # Add Widget
        self.grid_layout.addWidget(self.button_1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button_2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button_3, 2, 1, 1, 2)

        # Set Layout
        self.central_widget.setLayout(self.grid_layout)

        # Window config and Set Central Widget
        self.setWindowTitle('Meu título')
        self.resize(300, 200)
        self.setCentralWidget(self.central_widget)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Minha barra de status')

        # menuBar
        self.menu_bar = self.menuBar()

        # First Menu
        self.first_menu = self.menu_bar.addMenu('Primeiro Menu')

        # Actions
        self.first_action = self.first_menu.addAction('Primeira Ação')
        self.first_action.triggered.connect(self.change_status_bar_text)

        self.second_action = self.first_menu.addAction('Segunda Ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_checked)
        self.second_action.hovered.connect(self.second_action_checked)

    @Slot()
    def change_status_bar_text(self):
        self.status_bar.showMessage('Mudando a mensagem da status bar')

    @Slot()
    def second_action_checked(self):
        print("Checked:", self.second_action.isChecked())

    def make_button(self, text: str, style: dict) -> QPushButton:
        style_adjusted = re.sub(
            '[\\{\\}\']', '', str(style).replace(', ', '; ')
        )

        button = QPushButton(text)
        button.setStyleSheet(style_adjusted)

        return button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    app.exec()
