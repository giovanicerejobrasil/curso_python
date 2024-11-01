"""
Exercício - Salve sua classe em JSON

Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos

Faça em arquivos separados.
"""
import json
FILE_PATH = 'poo/aula_130.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def save(list):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(
            list,
            file,
            indent=2,
            ensure_ascii=True
        )


p1 = Person('Giovani', 27)
p2 = Person('Luanna', 24)
p3 = Person('Mel', 11)
p4 = Person('Malu', 3)

data = [vars(p1), vars(p2), vars(p3), vars(p4)]

save(data)
