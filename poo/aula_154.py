"""
Funções decoradoras e decoradores com classes
"""


def my_repr(self):
    class_name = type(self).__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'

    return class_repr


def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

# Usada como herança
# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'

#         return class_repr


@add_repr
class Teams:
    def __init__(self, name) -> None:
        self.name = name


@add_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name


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
