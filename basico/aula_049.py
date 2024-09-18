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

lista = [123, True, 'Giovani Brasil', 1.2, []]

print(lista)
print(lista[2].upper(), type(lista[2]))
print(type(lista))
print(bool(lista))

lista[2] = "Luanna"

print(lista[2])