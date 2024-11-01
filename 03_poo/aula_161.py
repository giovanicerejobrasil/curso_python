"""
dataclasses - O que são dataclasses?

O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.

Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass, asdict, astuple, field, fields


@dataclass()
class Person:
    _first_name: str = field(
        default='Missing',
        repr=True
    )
    _last_name: str = 'Not sent'
    _age: int = 100
    _addresses: list[str] = field(default_factory=list)

    # def __init__(self, first_name, last_name) -> None:
    #     self._first_name = first_name
    #     self._last_name = last_name
    #     self._complete_name_2 = 'SEM INIT AUTOMÁTICO'

    def __post_init__(self):
        self._complete_name_2 = f'{self._first_name} {self._last_name}'

    @property
    def complete_name(self):
        return f'{self._first_name} {self._last_name}'

    @complete_name.setter
    def complete_name(self, name):
        first_name, *last_name = name.split()
        self._first_name = first_name
        self._first_name = ' '.join(last_name)

        print(f'{first_name=} | {last_name=}')


@dataclass(frozen=True, repr=True, order=True)
class SignUp:
    user: str
    password: str


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


if __name__ == '__main__':
    p1 = Person('Giovani', 'Brasil')
    p2 = Person('Luanna', 'Paixão')
    p3 = Person()
    signup1 = SignUp('giovani.brasil', '123456')

    print_division('DATACLASS REPR')
    print(p1)
    print(p2)

    print_division('DATACLASS EQ', jump=True)
    print('p1 == p2 =>', p1 == p2)

    print_division('DATACLASS @PROPERTY AND SETTER', jump=True)
    print(p1.complete_name)
    p1.complete_name = 'Luanna Caroline Raiol Paixão'

    print_division('DATACLASS POST_INIT', jump=True)
    print(p2._complete_name_2)

    print_division('DATACLASS CONFIGURAÇÕES', jump=True)
    # signup1.user = 'teste' # Não pode atribuir com o frozen ativado
    print(signup1)  # Não tem repr com ele desativado
    # list_ = [SignUp('mel', '456'),
    #          SignUp('giovani', '123'),
    #          SignUp('malu', '654'),
    #          SignUp('luanna', '321')]
    # list_order = sorted(list_, reverse=True)
    # print()
    # print('', *list_order, '', sep='\n') # ordena com o order ativado

    print_division('DATACLASS ASDICT E ASTUPLE', jump=True)
    print(asdict(p1))
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p2))
    print(astuple(p2)[1])

    print_division('DATACLASS VALORES PADRÃO, FIELD E FIELDS', jump=True)
    print(p3)
    print('', fields(p3), sep='\n')
