"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado

lista_soma  = [2, 4, 6, 8]
"""

list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4]

list_sum = [
  x + y
  for x, y in zip(list_a, list_b)
]
print('MINHA SOLUÇÃO')
print(list_sum)

print('', '=' * 50, '', sep='\n')

list_sum = []
for i in range(
  len(list_a if len(list_a) < len(list_b) else list_b)
):
  list_sum.append(list_a[i] + list_b[i])
  
print('USANDO RANGE')
print(list_sum)

print('', '=' * 50, '', sep='\n')

list_sum = []
for i, _ in enumerate(
  list_a if len(list_a) < len(list_b) else list_b
):
  list_sum.append(list_a[i] + list_b[i])
  
print('USANDO ENUMERATOR')
print(list_sum)