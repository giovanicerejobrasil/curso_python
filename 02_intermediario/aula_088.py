"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis
"""

print(list(range(10)))

lista = []

for numero in range(10):
  lista.append(numero)
print(lista)

lista = [numero for numero in range(10)]
print(lista)

lista = [
  numero * 2
  for numero in range(10)
]
print(lista, '\n')

"""
Mapeamento em List comprehension
"""

produtos = [
    {'nome': 'Notebook', 'preco': 3565},
    {'nome': 'Monitor', 'preco': 980},
    {'nome': 'Teclado', 'preco': 250},
    {'nome': 'Mouse', 'preco': 150},
]
print(*produtos, '', sep='\n')

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] >= 300
  else {**produto, 'preco': produto['preco'] * 1.10}
  for produto in produtos
]
print(*novos_produtos, '', sep='\n')

"""
Filtro em List comprehension
"""

lista = [
  n for n in range(10)
  if n < 5
]
print(lista, '', sep='\n')

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.15}
  if produto['preco'] >= 300
  else produto
  for produto in produtos
  if (produto['preco'] * 1.10) >= 300
]
print(*novos_produtos, '', sep='\n')

"""
Vários For em List comprehension
"""

lista = []
for x in range(3):
  for y in range(3):
    lista.append((x, y))
print(lista, '', sep='\n')

lista = [
  (x, y)
  for x in range(3)
  for y in range(3)
]
print(lista, '', sep='\n')