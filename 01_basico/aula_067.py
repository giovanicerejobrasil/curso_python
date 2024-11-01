"""
CPF: 746.824.890-70

Coleta a soma dos 9 primeiros dígitos do CPF,
mais o primeiro dígito verificador,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

EX.: 746.824.890-70 (746824890)
  11 10 9  8  7  6  5  4  3  2
  7  4  6  8  2  4  8  9  0  7
  77 40 54 64 14 24 40 36 0  14

Somar todos os resultados:
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363

Multiplicar o resultado anterior por 10
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0

Se o resultado anterior for maior que 9:
  resultado é 0
Se não:
  resultado é o próprio número
"""

import re, sys

cpf = input('CPF [746.824.890-70]: ')
cpf = re.sub(r'[^0-9]', '', cpf)
nove_digitos = cpf[:9]

entrada_e_repetida = cpf == (cpf[0] * len(cpf))

if entrada_e_repetida:
  print('Digite um CPF válido!')
  sys.exit();

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

if cpf == novo_cpf:
  print(f'CPF {cpf} é válido!')
else:
  print(f'CPF {cpf} é inválido!')
  