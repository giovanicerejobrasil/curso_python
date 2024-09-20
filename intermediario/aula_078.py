"""
Exercício
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro
"""

def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(4))
print(quadruplicar(6))

