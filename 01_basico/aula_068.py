"""
Gerador de CPFs
"""

import random

for _ in range(20):
  nove_digitos = ''

  for i in range(9):
    nove_digitos += str(random.randint(0, 9))

  contador_regressivo_1 = 10
  resultado_1 = 0

  for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
  resultado_1 = (resultado_1 * 10) % 11
  digito_1 = resultado_1 if resultado_1 <= 9 else 0

  dez_digitos = nove_digitos + f'{resultado_1}'

  contador_regressivo_2 = 11
  resultado_2 = 0

  for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

  resultado_2 = (resultado_2 * 10) % 11
  digito_2 = resultado_2 if resultado_2 <= 9 else 0

  novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

  print(f'CPF Gerado: {novo_cpf}')