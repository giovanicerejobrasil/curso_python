"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
interir, apagar e listar valores da sua list
Não permita que o programa quebre com
erros de índicie inexistentes na lista
"""

import os

CONTINUAR = "Pressione enter para continuar!"

lista_compras = []

while True:
  os.system('clear')
  
  print('Lista de Compras - Python')
  print('Escolha as opções: ')
  print('[i] Inserir')
  print('[a] Apagar')
  print('[l] Listar')
  print('[s] Sair')

  escolha = input(':: ')

  if escolha.lower().startswith('s'):
    break

  elif escolha.lower().startswith('i'):
    print('Digite o item que deseja adicionar')
    lista_compras.append(input(':: '))

  elif escolha.lower().startswith('a'):
    for i in range(len(lista_compras)):
      print(f"[{i}] {lista_compras[i]}")

    print('Digite o índicie que deseja apagar')

    try:
      lista_compras.pop(int(input(':: ')))
      print('Item removido com sucesso')
    except ValueError:
      print('Por favor, digite um número inteiro!')
    except IndexError:
      print('O índicie digitado não existe!')
    except Exception:
      print('Erro desconhecido!')

    input(CONTINUAR)

  elif escolha.lower().startswith('l'):
    for i in range(len(lista_compras)):
      print(f"[{i}] {lista_compras[i]}")

    input('Pressione enter para continuar!')
  
  else:
    print('Nenhuma opção válida selecionada!')
    input(CONTINUAR)