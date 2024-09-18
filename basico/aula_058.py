"""
enumerate - Enumera iteráveis (índicies)
"""

lista = ['Giovani', 'Luanna', 'Malu', 'Mel']
print(lista)

print(enumerate(lista))

for indicie, nome in enumerate(lista):
  print(indicie, nome)