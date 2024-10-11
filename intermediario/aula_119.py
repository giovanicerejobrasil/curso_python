"""
JSON em python
"""
import json

person = {
    'nome': 'Giovani',
    'sobrenome': 'Brasil',
    'enderecos': [
        {'rua': 'Rua Álvarez', 'numero': 32},
        {'rua': 'Rua da Correção', 'numero': 55},
    ],
    'altura': 1.7,
    'numeros_preferidos': (11, 27, 32, 97, 147),
    'dev': True,
    'nada': None,
}

with open('intermediario/aula_119.json', 'w', encoding='utf-8') as file:
    json.dump(
        person,
        file,
        ensure_ascii=False,
        indent=2
    )

with open('intermediario/aula_119.json', 'r', encoding='utf-8') as file:
    people_decode = json.load(file)
    print(people_decode)
    print(type(people_decode))
    print(people_decode['nome'])
