"""
Digitar um número inteiro
Informar se o número é par ou impar
Caso não seja um número inteiro
Informar que não é um número inteiro
"""

numero = input('Digite um número: ')

if numero.isdigit():
  numero_int = int(numero)
  par_impar = numero_int % 2 == 0
  par_impar_texto = 'ímpar'

  if par_impar:
    par_impar_texto = 'par'
  
  print(f'O número {numero} é {par_impar_texto}!')

else:
  print(f'O valor digitado "{numero}" não é um número ou não é um número inteiro')