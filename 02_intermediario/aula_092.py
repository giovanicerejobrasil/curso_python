"""
dir, hasattr e getattr em Python
"""

string = 'Giovani'
metodo = 'upper'

print('DIR')
print(dir(string))
print()

if hasattr(string, metodo):
  print(f'Existe o método: {metodo}')
  print(getattr(string, metodo)())
else:
  print(f'Não existe o método: {metodo}')