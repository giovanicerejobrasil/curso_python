"""
Exercício
Digitar o nome
Digitar a idade
Se o nome e idade forem digitados:
  Exiba
    Seu nome é {nome}
    Seu nome invertido é {nome_invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do su nome é {primeira_letra}
    A última letra do seu nome é {ultima_letra}
Se não for digitado nome ou idade:
  Exiba
    Desculpe, você deixou campos vazios
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
  print('Desculpe, você deixou campos vazios')
else:
  print(f'Seu nome é {nome} e você tem {idade} anos de idade')
  print(f'Seu nome invertido é "{nome[::-1]}"')
  
  if ' ' in nome:
    print('Seu nome contém espaço')
  else:
    print('Seu nome NÃO contém espaço')
  
  print(f'Seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é "{nome[0]}"')
  print(f'A última letra do seu nome é "{nome[-1]}"')
