"""
Classes abstratas - Abstract Base Class (abc)

ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos. Também podem ter
métodos concretos por elas mesmas.

@abstractmethods são métodos que não têm corpo.

As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.

Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).

Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.
"""
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')

    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} | {self.__class__.__name__}')


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


log = LogPrintMixin()
log.log_error('HELLO TEXT ERROR')
