"""
Exercícios com funções
"""

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
"""
def multiplicar(*args):
  total = 1
  for num in args:
    total *= num
  return total

numeros = (2, 3, 4, 5, 6)
multiplicacao = multiplicar(*numeros)
print(f'A multiplicação de {numeros} é igual a {multiplicacao}')

"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def par_impar(numero):
  return f'O número {numero} é {'par' if numero % 2 == 0 else 'ímpar'}!'

print(par_impar(2))
print(par_impar(39))
print(par_impar(986))
print(par_impar(1537))