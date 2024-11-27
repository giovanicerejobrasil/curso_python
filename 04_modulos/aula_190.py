"""
sis.argv - Executando arquivos com argumentos no sistema
"""
import sys

arguments = sys.argv
arguments_qtd = len(arguments)

if arguments_qtd <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos: {arguments[1:]}')
        print(f'Faça alguma coisa com o {arguments[1]}')
        print(f'Faça outra coisa com o {arguments[2]}')
    except IndexError:
        print('Faltam argumentos')
