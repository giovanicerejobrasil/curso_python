"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.

Imutáveis: str, int, float, bool, tuple
Mutável: dict, list

pessoa = {
    'nome': 'Giovani',
    'sobrenome': 'Brasil',
    'idade': 27,
    'altura': 1.7,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

pessoa = dict(nome='Giovani', sobrenome='Brasil') -> não é muito usado
"""

pessoa = {
  'nome': 'Giovani',
  'sobrenome': 'Brasil',
  'idade': 27,
  'altura': 1.7,
  'endereços': [
      {'rua': 'tal tal', 'número': 123},
      {'rua': 'outra rua', 'número': 321},
  ],
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
  print(f'{chave}: {pessoa[chave]}')

print()
print('='*50)
print()

"""
Manipulando chaves e valores em dicionários
"""
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Giovani'
pessoa['sobrenome'] = 'Brasil'

del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
  print('NÃO EXISTE')
else:
  print(pessoa.get('sobrenome'))
