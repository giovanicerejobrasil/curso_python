"""
Criando Exceptions em Python Orientado a Objetos

Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.

A recomendação da doc é herdar de Exception.

https://docs.python.org/3/library/exceptions.html

Criando exceções (comum colocar Error ao final)

Levantando (raise) / Lançando (throw) exceções

Relançando exceções

Adicionando notas em exceções (3.12.5)
"""


class MyError(Exception):
    ...


class OtherError(Exception):
    ...


def raise_error():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Nota 1 de erro')
    exception_.add_note('Você errou na nota 2')

    raise exception_


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


try:
    raise_error()
except (MyError, ZeroDivisionError) as error:
    print_division(text='LEVANTANDO A EXCEÇÃO')

    print(error.__class__.__name__)
    print(error)

    print_division(text='RELANÇANDO A EXCEÇÃO', jump=True)

    exception_ = OtherError('Vou relançar esta exceção...')

    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Nota de relançamento')

    raise exception_ from error
