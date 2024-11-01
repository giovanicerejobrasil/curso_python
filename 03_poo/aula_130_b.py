"""
Exercício - Salve sua classe em JSON

Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos

Faça em arquivos separados.
"""
import json
from aula_130_a import FILE_PATH, Person


def load():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


data = load()

p1 = Person(**data[0])
p2 = Person(**data[1])
p3 = Person(**data[2])
p4 = Person(**data[3])

print(vars(p1))
print(vars(p2))
print(vars(p3))
print(vars(p4))
