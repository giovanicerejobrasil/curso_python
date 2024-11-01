"""
Abstração
Herança - é um
"""

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')

    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formatted_msg = f'{msg} | {self.__class__.__name__}'

        print('SALVANDO LOG...', msg)

        with open(LOG_FILE, 'a') as file:
            file.write(formatted_msg)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} | {self.__class__.__name__}')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Texto de erro')
    lp.log_success('Texto de sucesso')

    lf = LogFileMixin()
    lf.log_error('Texto de erro')
    lf.log_success('Texto de sucesso')
    print(LOG_FILE)
