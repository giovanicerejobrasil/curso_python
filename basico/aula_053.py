"""
Cuidados com dados mutáveis
= - Copiando o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
"""

nome = 'Giovani'
nome_substituido = nome
nome = 'Luanna'

print(nome, 'ID:', id(nome))
print(nome_substituido, 'ID:', id(nome_substituido))

lista_a = ['Giovani', 'Luanna', 27, 24]
lista_b = lista_a.copy()

lista_a[0] = 'Alterado'

print('Lista B:', lista_b)