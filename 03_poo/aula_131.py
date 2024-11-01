"""
Métodos de classe + factories

São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro
parâmetro, recebemos a própria classe
"""


class Person:
    current_year = 2024  # atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hey')

    @classmethod
    def create_with_50_years(cls, name):
        return cls(name, 50)

    @classmethod
    def creat_without_name(cls, age):
        return cls('Anônima', age)


def print_division(text='', num_repeat=50):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division('PRINT DIRETO NA CLASSE', num_repeat=30)

print(Person.current_year)

print_division('CHAMANDO O MÉTODO DIRETO NA CLASSE', num_repeat=30)

p1 = Person('Giovani', 27)
Person.class_method()

print_division(
    'INSTANCIANDO UMA CLASSE ATRAVÉS DO \n"@classmethod"', num_repeat=30)

p2 = Person.create_with_50_years('Mel')
print(vars(p2))

p3 = Person.creat_without_name(27)
print(vars(p3))
