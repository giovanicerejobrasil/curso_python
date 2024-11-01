"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros
podem ter valores padrão.
Caso o valor seja enviado para o
parâmetro, o valor padrão será usado.
"""

def soma(x, y, z=None):
  if z is not None:
    print(f'{x=} + {y=} + {z=}', '|', x + y + z)
  else:
    print(f'{x=} + {y=}', '|', x + y)

soma(5, 2)
soma(12, 33)
soma(137, 269)
soma(7, 9, 2)
soma(y=7, z=9, x=2)