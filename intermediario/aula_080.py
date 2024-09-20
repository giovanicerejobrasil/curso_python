"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

pessoa = {
  'nome': 'Giovani',
  'sobrenome': 'Brasil',
  'idade': 27
}

print('Quantidade:', len(pessoa))
print('Chaves:', tuple(pessoa.keys()))
print('Valores:', tuple(pessoa.values()))
print('Itens:', tuple(pessoa.items()))

pessoa.setdefault('sexo', None)
print(pessoa['sexo'])

print('\n' + '=' * 50 + '\n')

for valor in pessoa:
  print(valor)
print()
for valor in pessoa.values():
  print(valor)
print()
for chave, valor in pessoa.items():
  print(f'{chave}: {valor}')

print('\n' + '=' * 50 + '\n')

import copy

d1 = {
  'c1': 1,
  'c2': 2,
  'l1': [0, 1, 2]
}

d2 = d1.copy() # => Cópia rasa (Shallow Copy)
# d2 = copy.copy(d1) # => Cópia rasa (Shallow Copy)
# d2 = copy.deepcopy(d1) # => Cópia Profunda
d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)

print('\n' + '=' * 50 + '\n')

p1 = {
  'nome': 'Giovani',
  'sobrenome': 'Brasil',
}

print(p1)
print(p1.get('idade', 18))
print()

nome = p1.pop('nome')
print(nome)
print(p1)
print()

p1 = {
  'nome': 'Giovani',
  'sobrenome': 'Brasil',
}

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
print()

# p1.update({
#   'nome_meio': 'Cerejo',
#   'sobrenome': 'Brasil',
# })
# print(p1)

# p1.update(
#   nome_meio = 'Cerejo',
#   sobrenome = 'Brasil',
#   idade = 27
# )
# print(p1)

# tupla = (('nome_meio','Cerejo'),('sobrenome','Brasil'),('idade',27))
# p1.update(tupla)
# print(p1)

lista = [['nome_meio','Cerejo'],['sobrenome','Brasil'],['idade',27]]
p1.update(lista)
print(p1)