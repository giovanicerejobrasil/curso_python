"""
abstractmethod para qualquer método já decorado (@property e setter)

É possível criar @property @property.setter @classmethod

@staticmethod e métodos normais como abstratos, para isso use @abstractmethod como decorator mais interno.

Foo - Bar são palavras usadas como placeholder para palavras que podem mudar na programação.
"""
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('SOU INÚTIL')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


foo = Foo('BAR')
print(foo.name)