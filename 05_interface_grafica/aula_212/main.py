import sys
import time
import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QThread, Signal
from ui_worker import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'

        self.started.emit(value)

        for i in range(random.randrange(1, 10)):
            value = str(i)

            self.progressed.emit(value)
            time.sleep(1)

        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.__count: int = 0
        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self.__worker = Worker1()
        self.__thread = QThread()

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        self.__worker.moveToThread(self.__thread)

        # Run
        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        self.__thread.started.connect(self.__worker.run)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        self.__worker.finished.connect(self.__thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        self.__thread.finished.connect(self.__thread.deleteLater)
        self.__worker.finished.connect(self.__worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        self.__worker.started.connect(self.worker1Started)
        self.__worker.progressed.connect(self.worker1Progressed)
        self.__worker.finished.connect(self.worker1Finished)

        # Inicializa a thread
        self.__thread.start()

    def hardWork2(self):
        self.__worker2 = Worker1()
        self.__thread2 = QThread()

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        self.__worker2.moveToThread(self.__thread2)

        # Run
        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        self.__thread2.started.connect(self.__worker2.run)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        self.__worker2.finished.connect(self.__thread2.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        self.__thread2.finished.connect(self.__thread2.deleteLater)
        self.__worker2.finished.connect(self.__worker2.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        self.__worker2.started.connect(self.worker1Started)
        self.__worker2.progressed.connect(self.worker1Progressed)
        self.__worker2.finished.connect(self.worker1Finished)

        # Inicializa a thread
        self.__thread2.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker1 iniciado')

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('worker1 em progresso')

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('worker1 finalizado')

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker2 iniciado')

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('worker2 em progresso')

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print('worker2 finalizado')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()

    myWidget.show()
    app.exec()
