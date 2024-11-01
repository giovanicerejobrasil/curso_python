"""
Funções decoradoras e decoradores com métodos
"""


def my_repr(self):
    class_name = type(self).__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'

    return class_repr


def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def my_planet(method):
    def internal(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'Você está em casa!'

        return result
    return internal


@add_repr
class Teams:
    def __init__(self, name) -> None:
        self.name = name


@add_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name

    @my_planet
    def speak_name(self):
        return f'O planeta é {self.name}'


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


brazil = Teams('Brasil')
uk = Teams('Inglaterra')

earth = Planet('Terra')
mars = Planet('Marte')

print_division(text='TIMES')
print(brazil)
print(uk)

print_division(text='PLANETAS', jump=True)
print(earth)
print(mars)

print_division(text='NOME DOS PLANETAS', jump=True)
print(earth.speak_name())
print(mars.speak_name())
