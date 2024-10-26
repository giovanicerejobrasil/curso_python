"""
__new__ e __init__ em classes Python

__new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.

__new__ ❗️DEVE retornar o novo objeto❗️

__init__ é o método responsável por inicializar a instância. Por isso, init recebe self.

__init__ ❗️NÃO DEVE retornar nada (None)❗️object é a super classe de uma classe
"""


class A:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        return instance

    def __init__(self, x) -> None:
        self.x = x
        print('__INIT__')

    def __repr__(self) -> str:
        return 'A()'


a = A(123)
print(a)
print(a.x)
