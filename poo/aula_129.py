"""
__dict__ e vars para atributos de instância
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
print(p1.__dict__)
print(vars(p1))

print_division()

p1.__dict__['other'] = 'atributo'
p1.__dict__['name'] = 'Outro Nome'
print(p1.__dict__)
print(vars(p1))

print_division()

data_2 = {'name': 'Luanna', 'age': 24}
p2 = Person(**data_2)

print(vars(p2))
