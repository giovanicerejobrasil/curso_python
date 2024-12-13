"""
Packaging PySide6 applications for Windows with PyInstaller & InstallForge:
https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/

PyInstaller Doc:
https://pyinstaller.org/en/stable/
"""
import sys

from main_window import MainWindow
from display import Display
from info import Info
from buttons import ButtonsGrid

from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme

if __name__ == '__main__':
    # Criação da aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Tema da calculadora
    setupTheme(app)

    # Definição do ícone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Ajuste de tela
    window.adjustFixedSize()

    # execução da aplicação
    window.show()
    app.exec()
