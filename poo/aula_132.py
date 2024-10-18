"""
@staticmethod (métodos estáticos) são inúteis em Python =)

Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.

Em resumo, são funções que existem dentro da sua classe.
"""


class Class:
    @staticmethod
    def static_method(*args, **kwargs):
        print('Hi', args, kwargs)


def function(*args, **kwargs):
    print('Hi', args, kwargs)


c1 = Class()
c1.static_method(1, 2, 3)
function(1, 2, 3)
Class.static_method(named=321)
function(named=321)
