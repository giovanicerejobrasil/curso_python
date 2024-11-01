"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índicies e fatiamento
Métodos úteis: 
  append - Adiciona um item ao final
  insert - Adiciona um item no índicie escolhido
  pop - Remove do final ou do índicie escolhido
  del - Apaga um índicie
  clear - Limpa a lista
  extend - Estende a lista
  + - Concatena listas
Create Read Update Delete = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Giovani')

print(lista)

nome = lista.pop()

print(lista, nome)

lista.append(1233)

print(lista)

del lista[-1]

print(lista)

lista.insert(0, 5)

print(lista)

lista.clear()

print(lista)