"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome = ''):
  return f'{msg}{f', {nome}' if nome else ''}!'

def executa(funcao, *args):
  return funcao(*args)

var = saudacao('Bom dia')
print(var)

var_2 = saudacao
print(var_2('Boa tarde'))

var_3 = executa(saudacao, 'Boa noite', 'Giovani')
print(var_3)