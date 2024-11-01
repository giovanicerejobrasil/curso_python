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

lista = [10, 20, 30, 40, 50]
lista[2] = 300

print(lista)
print(lista[2])

del lista[2]

print(lista)
print(lista[2])

lista.append(60)
lista.append(70)

print(lista)

ultimo_valor = lista.pop()

print(lista, 'Removido:', ultimo_valor)

ultimo_valor = lista.pop(2)

print(lista, 'Removido:', ultimo_valor)