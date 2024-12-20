"""
Metaclasses são o tipo das classes

EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)

Então, qual é o tipo de uma classe? (type)

Seu objeto é uma instância da sua classe

Sua classe é uma instância de type (type é uma metaclass)
type('Name', (Bases,), __dict__)

Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
__new__ da metaclass é chamado e cria a nova classe
__call__ da metaclass é chamado com os argumentos e chama:
        __new__ da class com os argumentos (cria a instância)
        __init__ da class com os argumentos
__call__ da metaclass termina a execução

Métodos importantes da metaclass
__new__(mcs, name, bases, dct) (Cria a classe)
__call__(cls, *args, **kwargs) (Cria e inicializa a instância)

"Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar. Se você quer saber se precisa delas, não precisa (as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de uma explicação sobre o porquê)."
— Tim Peters (CPython Core Developer)
"""

# Classe criada por type
# Foo = type('Foo', (object,), {})


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        print('', *cls.__dict__, '', sep='\n')

        if 'speak' not in cls.__dict__ or \
                not callable(cls.__dict__['speak']):
            raise NotImplementedError('The "speak" method is NOT implemented')

        return cls

    def __call__(cls, *args, **kwargs):
        instance_ = super().__call__(*args, **kwargs)

        if 'name' not in instance_.__dict__:
            raise NotImplementedError(
                'The "name" attribute is NOT implemented')

        return instance_


class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instance_ = super().__new__(cls)

        return instance_

    def __init__(self, name):
        print('MEU INIT')
        self.name = name

    def speak(self):
        print('FALANDO...')


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division('CLASSE PERSON', jump=True)
p1 = Person('Giovani')

print_division('ATRIBUTOS DA METACLASS', jump=True)
print('p1:', p1.attr)
print('Person:', Person.attr)
print(p1)
