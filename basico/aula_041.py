"""
Calculadora com while
"""

while True:
  sair = ''
  operadores_permitidos = '+ - / // % * **'
  resultado = 0

  numero_1 = input('Digite o primeiro número: ')
  numero_2 = input('Digite o segundo número: ')
  operador = input(f'Digite a operação [{operadores_permitidos}]: ')

  try:
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
    numeros_validos = True
  except Exception as error:
    numeros_validos = False

  if not numeros_validos:
    print('Um ou ambos os números são inválidos\n')
    continue

  if operador not in operadores_permitidos or len(operador) > 1:
    print('Operador digitado inválido\n')
    continue

  if operador == '+':
    resultado = numero_1 + numero_2
  elif operador == '-':
    resultado = numero_1 - numero_2
  elif operador == '/':
    resultado = numero_1 / numero_2
  elif operador == '//':
    resultado = numero_1 // numero_2
  elif operador == '%':
    resultado = numero_1 % numero_2
  elif operador == '*':
    resultado = numero_1 * numero_2
  elif operador == '**':
    resultado = numero_1 ** numero_2

  print(f"O resultado de {numero_1} {operador} {numero_2} = {resultado}\n")

  sair = input('Deseja sair? [s]im [n]ão: ').lower().startswith('s')
  
  if sair:
    break
