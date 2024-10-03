"""
Exercício - adiando a execução de funções
"""

def soma(x, y):
  return x + y

def multiplica(x, y):
  return x * y

def cria_funcao(funcao, x):
  def funcao_interna(y):
    return funcao(x, y)
  
  return funcao_interna

soma_por_cinco = cria_funcao(soma, 5)
multiplica_por_10 = cria_funcao(multiplica, 10)

print(soma_por_cinco(10))
print(multiplica_por_10(10))