import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow
from typing import cast


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeText)
        self.lineName.installEventFilter(self)

    def changeText(self):
        text = self.lineName.text()

        self.labelResult.setText(text)

        self.lineName.clear()
        self.lineName.setFocus()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
