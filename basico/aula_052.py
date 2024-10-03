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

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)
