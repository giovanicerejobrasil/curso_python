"""
class - Classes são moldes para criar novos objetos

As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

Por convenção, usamos PascalCase para nomes de
classes.
"""

# string = 'Giovani'  # str
# print(string.upper())
# print(isinstance(string, str))


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


person_1 = Person('Giovani', 'Brasil')
# person_1.first_name = 'Giovani'
# person_1.last_name = 'Brasil'

person_2 = Person('Luanna', 'Paixão')
# person_2.first_name = 'Luanna'
# person_2.last_name = 'Paixão'

print(person_1)
print(person_1.first_name)
print(person_1.last_name)
print()

print(person_2)
print(person_2.first_name)
print(person_2.last_name)
