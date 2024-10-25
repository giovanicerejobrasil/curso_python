"""
Herança Múltipla - Python Orientado a Objetos

Quer dizer que no Python, uma classe pode estender várias outras classes.

Herança simples:

Animal -> Mamifero -> Humano -> Pessoa -> Cliente

Herança múltipla e mixins

Log -> FileLog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, FileLog)

A, B, C, D
D(B, C) - C(A) - B(A) - A

método -> falar
          A
    	// \\
       B     C
        \\ //
          D

Python 3 usa C3 superclass linearization para gerar o mro.

Você não precisa estudar isso (é complexo)
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos

Use o método de classe Classe.mro() Ou o atributo __mro__ (Dunder - Double Underscore)
"""


class A:
    ...

    def who_am_i(self):
        print('A')


class B(A):
    ...

    # def who_am_i(self):
    #     print('B')


class C(A):
    ...

    def who_am_i(self):
        print('C')


class D(B, C):
    ...

    # def who_am_i(self):
    #     print('D')


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


d = D()
print_division('QUEM EU SOU')
d.who_am_i()

print_division('MRO', jump=True)
print(*D.mro(), sep='\n')
