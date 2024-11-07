"""
os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
"""
import math
import os
from itertools import count


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


def format_size(bytes_size: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if bytes_size <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    sizes_abbreviation = ("B", "KB", "MB", "GB", "TB", "PB")
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    sizes_abbreviation_index = int(math.log(bytes_size, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    power = base ** sizes_abbreviation_index
    # Nosso tamanho final
    final_size = bytes_size / power
    # A abreviação que queremos
    size_abbreviation = sizes_abbreviation[sizes_abbreviation_index]
    return f'{final_size:.2f} {size_abbreviation}'


path = os.path.join('/home', 'giovani-brasil',
                    'Desktop', 'Development', 'EXEMPLE')
counter = count()

for roots, dirs, files in os.walk(path):
    the_counter = next(counter)

    print(the_counter, '=>', roots)

    for dir_ in dirs:
        print(' ' * 3, the_counter, '| Dir =>', dir_)

    for file_ in files:
        full_path_file = os.path.join(roots, file_)
        # size_ = os.path.getsize(full_path_file)
        stats = os.stat(full_path_file)
        size_ = stats.st_size

        print(' ' * 6, the_counter, '| File =>',
              file_, f'({format_size(size_)})')
