"""
Atributos de classe
"""


class Person:
    CURRENT_YEAR = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_born_year(self):
        return Person.CURRENT_YEAR - self.age


def print_division(num_repeat=50):
    print('', '=' * num_repeat, '', sep='\n')


p1 = Person('Giovani', 27)
p2 = Person('Luanna', 24)

print(f'Ano atual: {Person.CURRENT_YEAR}')
print_division()

print(f'O ano de nascimento de {p1.name} é {p1.get_born_year()}')

print_division()

print(f'O ano de nascimento de {p2.name} é {p2.get_born_year()}')
