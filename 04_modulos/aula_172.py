"""
os.path trabalha com caminhos em Windows, Linux e Mac
Doc: https://docs.python.org/3/library/os.path.htmlodule-os.path

os.path é um módulo que fornece funções para trabalhar com caminhos de
arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
entre esses sistemas.

Exemplos do os.path:
os.path.join: junta strings em um único caminho. Desse modo,
os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
'pasta1/pasta2/arquivo.txt' no Linux ou Mac,
e 'pasta1\\pasta2\\arquivo.txt' no Windows.
os.path.split: divide um caminho uma tupla (diretório, arquivo).

Por exemplo, os.path.split('/home/user/arquivo.txt')
retornaria ('/home/user', 'arquivo.txt').

os.path.exists: verifica se um caminho especificado existe.
os.path só trabalha com caminhos de arquivos e não faz nenhuma operação de
entrada/saída (I/O) com arquivos em si.
"""
import os


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division(text='OS JOIN')
path = os.path.join('/home/giovani-brasil', 'Desktop',
                    'Development', 'tests', 'file.txt')
print(path)

print_division(text='OS SPLIT & SPLITEXT', jump=True)
directory, file = os.path.split(path)
file_path, extension_file = os.path.splitext(file)
print(directory)
print(file)
print(file_path)
print(extension_file)

print_division(text='OS EXISTS', jump=True)
print(os.path.exists(directory))

print_division(text='OS ABSPATH', jump=True)
print(os.path.abspath('.'))


print_division(text='OS BASENAME & DIRNAME', jump=True)
print(path)
print(os.path.basename(path))
print(os.path.basename(directory))
print(os.path.dirname(path))
