"""
Desempacotando em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')
salas = [
  ['Caique', 'Brenda', ],
  ['Mayara', ],
  ['Giovani', 'Luanna', 'Malu', 'Mel'],
]

p, b, *_, pn, u = lista
print(p, u, pn)

for nome in lista:
  print(nome, end=' ')
print()

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')