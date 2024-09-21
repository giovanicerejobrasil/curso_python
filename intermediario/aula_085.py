"""
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
"""

lista = [4,32,1,34,5,6,6,21]
print(lista)

lista.sort(reverse=True)
print(lista)

lista_2 = sorted(lista)
print(lista_2)

print('\n' + '=' * 50 + '\n')

lista = [
    {'nome': 'Luanna', 'sobrenome': 'Paixão'},
    {'nome': 'Malu', 'sobrenome': 'Brasil'},
    {'nome': 'Mel', 'sobrenome': 'Paixão'},
    {'nome': 'Giovani', 'sobrenome': 'Brasil'},
    {'nome': 'Mayara', 'sobrenome': 'Vaz'},
]

"""
Sem função lambda
def ordenar(item):
  return item['nome']

lista.sort(key=ordenar)
"""

def exibir(lista):
  for item in lista:
    print(item)

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print('Ordenado pelo nome:')
exibir(l1)

print('\n' + '=' * 50 + '\n')

print('Ordenado pelo sobrenome:')
exibir(l2)