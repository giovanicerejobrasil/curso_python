"""
argparse.ArgumentParser para argumentos mais complexos
Tutorial Oficial:
https://docs.python.org/pt-br/3/howto/argparse.html
"""
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra o "Hello World!" na tela',
    # type=str,  # Tipo do argumento
    metavar='STRING',
    # default='Hello World, Stranger!',  # Valor padrão
    required=False,
    action='append',  # Recebe o mesmo argumento mais de uma vez
    # nargs='+'  # Recebe mais de um valor no argumento
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de -b')
    print(args.basic)
else:
    print('Valor de -b:', args.basic)
    print(f'Hello World, {args.basic}!')

print(args.verbose)
