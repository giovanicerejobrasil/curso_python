from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    # Configura o estilo da Label
    def configStyle(self) -> None:
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
