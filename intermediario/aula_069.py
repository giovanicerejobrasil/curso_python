"""
Introdução às funções (def) em Python

Funções são trechos de código usados
para replicar determinadas ações ao longo
do seu código.

Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.

Por padrão, funções Python retornam None (nada).
"""

def imprimir(a, b, c):
  print(f'Parâmetro: {a} {b} {c}')

imprimir('A', 'B', 'C')
imprimir(1, 2, 3)

def saudacao(nome='Anônimo'):
  print(f'Olá, {nome}!')

saudacao('Giovani')
saudacao('Luanna')
saudacao()