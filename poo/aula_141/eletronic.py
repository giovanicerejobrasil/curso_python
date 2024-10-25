from log import LogFileMixin


class Eletronic:
    def __init__(self, name) -> None:
        self._name = name
        self._on = False

    def on(self):
        if not self._on:
            self._on = True

    def off(self):
        if self._on:
            self._on = False


class Smartphone(Eletronic, LogFileMixin):
    def on(self):
        super().on()

        if self._on:
            msg = f'{self._name} está ligado'
            self.log_success(msg)

    def off(self):
        super().off()

        if not self._on:
            msg = f'{self._name} está desligado'
            self.log_error(msg)
