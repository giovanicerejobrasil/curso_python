"""
os.walk para navegar de caminhos de forma recursiva

os.walk é uma função que permite percorrer uma estrutura de diretórios de
maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
três elementos:
  - o diretório atual (root)
  - uma lista de subdiretórios (dirs)
  - uma lista dos arquivos do diretório atual (files).
"""
import os
from itertools import count


path = os.path.join('/home', 'giovani-brasil',
                    'Desktop', 'Development', 'EXEMPLE')
counter = count()

for roots, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, '=>', roots)

    for dir_ in dirs:
        print('  ', the_counter, '| Dir =>', dir_)

    for file_ in files:
        print('  ', the_counter, '| File =>', file_)
