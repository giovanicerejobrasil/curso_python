"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 1 == 2
variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)

digito = 11
novo_digito = digito if digito <= 9 else 0

print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')