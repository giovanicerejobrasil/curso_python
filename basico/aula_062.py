"""
Lista de listas e seus índicies
"""

salas = [
  # 0         1
  ['Caique', 'Brenda', ], # 0
  # 0
  ['Mayara', ], # 1
  # 0          1         2       3      4
  ['Giovani', 'Luanna', 'Malu', 'Mel', (27, 24, 2, 11)], # 2
]

print(salas)
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][4][2])

for indice, sala in enumerate(salas):
  print(f"Sala: {indice}")
  for aluno in sala:
    print(aluno)