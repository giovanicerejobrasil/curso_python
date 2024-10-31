"""
namedtuples - tuplas imutáveis com nomes para valores

Usamos namedtuples para criar classes de objetos que são apenas um agrupamento
de atributos, como classes normais sem métodos, ou registros de bases de
dados, etc.

As namedtuples são imutáveis assim como as tuplas.
https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
https://brasilescola.uol.com.br/curiosidades/baralho.htm
"""
from collections import namedtuple
from typing import NamedTuple

Card = namedtuple(
    'Card', ['value', 'suit'],
    defaults=['VALOR', 'NAIPE']
)


class NewCard(NamedTuple):
    value: str = 'VALOR'
    suit: str = 'NAIPE'


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


ace_spades = Card('A', '♠️')

print_division('COLLECTIONS NAMEDTUPLE')
print(ace_spades)
print(ace_spades.value)
print(ace_spades.suit)
print(ace_spades._fields)
print(ace_spades._field_defaults)
print(ace_spades._asdict())

print_division('TYPING NAMEDTUPLE', jump=True)
ace_diamond = NewCard('A', '♦️')
print(ace_diamond)
print(ace_diamond.value)
print(ace_diamond.suit)
print(ace_diamond._fields)
print(ace_diamond._field_defaults)
print(ace_diamond._asdict())
