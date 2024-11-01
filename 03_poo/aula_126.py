"""
Escopo da classe e de métodos da classe
"""


class Animal():
    def __init__(self, name):
        self.name = name

        variable = 'Teste'
        print(variable)

    def eating(self, food):
        return f'O {self.name} está comendo {food}!'

    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)


def print_division(num_repeat=50):
    print('', '=' * num_repeat, '', sep='\n')


lion = Animal('Leão')
print(lion.name)
print(lion.execute('manga'))
