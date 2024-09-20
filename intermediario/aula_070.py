"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
  print(f'{x=} + {y=} + {z=}', '|', 'x + y + z =', x + y + z)

soma(2, 3, 4)
soma(y=3, z=4, x=2)
