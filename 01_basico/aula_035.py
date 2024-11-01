"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
  nome = input('Qual o seu nome: ')

  if not nome or nome == 'sair':
    condicao = False
  else:
    print(f"Seu nome é {nome}.")