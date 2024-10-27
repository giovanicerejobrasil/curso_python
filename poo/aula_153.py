"""
Context Manager com função - Criando e usando gerenciadores de contexto
"""
from contextlib import contextmanager


@contextmanager
def my_open_file(file_path, mode):
    try:
        print(f'Abrindo o arquivo ({file_path})...')
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as error:
        print('ERROR: ', error)
    finally:
        print(f'Fechando o arquivo ({file_path})...')
        file.close()


with my_open_file('poo/aula_153.txt', 'w') as file:
    file.write('LINHA 1\n')
    file.write('LINHA 2\n', 123)
    file.write('LINHA 3\n')
    print("WITH", file)
