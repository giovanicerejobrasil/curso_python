from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configuração do Layout básico
        self.cWidget = QWidget()
        self.vLayout = QVBoxLayout()

        self.cWidget.setLayout(self.vLayout)

        self.setCentralWidget(self.cWidget)

        # Título da janela
        self.setWindowTitle('Calculadora PySide6')

    # Configura o tamanho e ajustes da janela
    def adjustFixedSize(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adiciona um widget ao layout vertical
    def addWidgetToVLayout(self, widget: QWidget) -> None:
        self.vLayout.addWidget(widget)

    def makeMessageBox(self):
        return QMessageBox(self)
