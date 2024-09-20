"""
Higher Order Functions
Funções de primeira classe

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
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