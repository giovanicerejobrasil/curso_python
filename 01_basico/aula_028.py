"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar o  código
"""

numero_str = input('Digite um numero para dobrar: ')

try:
  numero_float = float(numero_str)
  print(f'O dobro do número {numero_str} é {numero_float * 2:.2f}')
except:
  print('Isso não é uma número,')