import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main_window import MainWindow
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    # Configura o estilo do botão
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)

        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self,
        display: 'Display',
        info: 'Info',
        window: 'MainWindow',
        * args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self.__grid_mask: list[list[str]] = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.display: Display = display
        self.info: Info = info
        self.__equation: str = ''
        self.__equationInitialValue: str = '0'
        self.__left: float | None = None
        self.__right: float | None = None
        self.__operator: str | None = None
        self.__window: MainWindow = window

        self.equation = self.__equationInitialValue

        self.__makeGrid()

    # Get
    @property
    def equation(self) -> str:
        return self.__equation

    # Set
    @equation.setter
    def equation(self, value) -> None:
        self.__equation = value
        self.info.setText(value)

    # Cria a grid dos botões apartir de uma máscara
    def __makeGrid(self) -> None:
        self.display.eqPressed.connect(self.__configRightAndEqual)
        self.display.delPressed.connect(self.__backspace)
        self.display.clearPressed.connect(self.__clear)
        self.display.inputPressed.connect(self.__insertTextToDisplay)
        self.display.operatorPressed.connect(self.__configLeftAndOperation)
        self.display.inverterPressed.connect(self.__invertNumber)

        for row, items in enumerate(self.__grid_mask):
            for column, text in enumerate(items):
                button = Button(text)

                if not isNumOrDot(text) and not isEmpty(text):
                    button.setProperty('cssClass', 'specialButton')
                    self.__configSpecialButton(button)

                self.addWidget(button, row, column)

                slot = self.__makeSlot(self.__insertTextToDisplay, text)
                self.__connectClicked(button, slot)

    # Conecta o Slot ao click do botão
    def __connectClicked(self, button: Button, slot) -> None:
        button.clicked.connect(slot)

    # Configura os botãoes especiais (operadores)
    def __configSpecialButton(self, button: Button) -> None:
        text = button.text()

        if text == 'C':
            self.__connectClicked(button, self.__clear)

        if text == '◀':
            self.__connectClicked(
                button,
                self.__makeSlot(self.__backspace)
            )

        if text == 'N':
            self.__connectClicked(button, self.__invertNumber)

        if text in '+-/*^':
            self.__connectClicked(
                button,
                self.__makeSlot(self.__configLeftAndOperation, text)
            )

        if text == '=':
            self.__connectClicked(
                button,
                self.__makeSlot(self.__configRightAndEqual)
            )

    # Cria um Slot
    def __makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_) -> None:
            func(*args, **kwargs)
        return realSlot

    # Inverte o número atual
    @Slot()
    def __invertNumber(self) -> None:
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newNumber = convertToNumber(displayText) * -1

        self.display.setText(str(newNumber))
        self.display.setFocus()

    # Insere o texto do botão no display
    def __insertTextToDisplay(self, text: str) -> None:
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    # Limpa o campo de texto e reseta as variáveis
    @Slot()
    def __clear(self) -> None:
        self.__left = None
        self.__right = None
        self.__operator = None
        self.equation = self.__equationInitialValue

        self.display.clear()
        self.display.setFocus()

    # Apaga o último número ou ponto digitado
    @Slot()
    def __backspace(self):
        self.display.backspace()
        self.display.setFocus()

    # Adiciona o operador, o número da esquerda e limpa o campo de texto
    @Slot()  # type: ignore
    def __configLeftAndOperation(self, text) -> None:
        displayText = self.display.text()

        self.display.clear()

        if not isValidNumber(displayText) and self.__left is None:
            self.__showError('Você não digitou nada')
            return

        if self.__left is None:
            self.__left = convertToNumber(displayText)

        self.__operator = text
        self.equation = f'{self.__left} {self.__operator}'

        self.display.setFocus()

    # Adiciona o número à direita, faz o cálculo e obtém o resultado e
    # limpa o display
    @Slot()
    def __configRightAndEqual(self) -> None:
        displayText = self.display.text()

        __error: bool = True
        result: float = 0.0

        if not isValidNumber(displayText) or self.__left is None:
            self.__showError('Conta incompleta!')
            return

        self.__right = convertToNumber(displayText)
        self.equation = f'{self.__left} {self.__operator} {self.__right}'

        try:
            if '^' in self.equation and isinstance(self.__left, (float, int)):
                result = math.pow(self.__left, self.__right)
            else:
                result = convertToNumber(eval(self.equation))

            __error = False
        except ZeroDivisionError:
            self.__showError('Divizão por ZERO não permitida!')
            return
        except OverflowError:
            self.__showError('Cálculo excede a memória!')
            return

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        self.__left = convertToNumber(result)
        self.__right = None

        if __error:
            self.__left = None

        self.display.setFocus()

    # Facilita a criação de um QMessageBox
    def __makeDialog(self, text: str):
        messageBox = self.__window.makeMessageBox()
        messageBox.setText(text)

        return messageBox

    # Exibe uma caixa de diálogo com o erro obtido
    def __showError(self, text):
        messageBox = self.__makeDialog(text)
        messageBox.setIcon(messageBox.Icon.Critical)

        messageBox.exec()

        self.display.setFocus()

    # Exibe uma caixa de diálogo com uma informação obtido
    def __showInfo(self, text):
        messageBox = self.__makeDialog(text)
        messageBox.setIcon(messageBox.Icon.Information)

        messageBox.exec()

        self.display.setFocus()
