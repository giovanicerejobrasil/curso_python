"""
Herança simples - Relações entre classes

Associação - usa, Agregação - tem

Composição - É dono de, Herança - É um

Herança vs Composição

Classe principal (Pessoa)
  -> super class, base class, parent class

Classes filhas (Cliente)
  -> sub class, child class, derived class
"""


class Person:
    cpf = '123'

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def show_name_class(self):
        print(f'{self.first_name} {self.last_name} |', self.__class__.__name__)


class Client(Person):
    def show_name_class(self):
        print('CLASSE CLIENTE')
        print(f'{self.first_name} {self.last_name} |', self.__class__.__name__)


class Student(Person):
    cpf = 'abc'


cl1 = Client('Giovani', 'Brasil')
al1 = Student('Luanna', 'Paixão')

cl1.show_name_class()
al1.show_name_class()

print(al1.cpf)
