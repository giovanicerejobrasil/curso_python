"""
Exercício - Unir listas

Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""
from itertools import zip_longest

def zipper(list_1, list_2):
  shortest_list_len = min(len(list_1), len(list_2))
  
  return [
    (list_1[i], list_2[i]) for i in range(shortest_list_len)
  ]
  
list_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_2 = ['BA', 'SP', 'MG', 'RJ']
print('MY FUNCTION ZIPPER')
print(zipper(list_1, list_2))

print('', '=' * 50, '', sep='\n')

print('PYTHON FUNCTION ZIP')
print(list(zip(list_1, list_2)))

print('', '=' * 50, '', sep='\n')

print('PYTHON FUNCTION ITERTOOLS ZIP LONGEST')
print(list(zip_longest(list_1, list_2, fillvalue='SEM CIDADE')))