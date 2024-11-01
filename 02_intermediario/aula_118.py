"""
Criando arquivos com Python + Context Manager with

Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)

Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)

Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
"""
import os


def print_division(num_repeat=50):
    print('', '=' * num_repeat, '', sep='\n')


def print_iterator(name, iterator):
    print(name)
    print(*iterator, sep='\n')


# Caminho completo
# file_path = "/home/giovani-brasil/Desktop/Development/udemy/luiz_otavio_miranda/curso_python/"
file_path = "intermediario/aula_118.txt"

# file = open(file_path, 'w')
# file.close()

with open(file_path, 'w') as file:
    print('ESCRITA (w)')
    file.write('Linha 1\n')
    file.write('Linha 2\n')

    print('WRITE LINES')
    file.writelines(
        ('Linha 3\n', 'Linha 4\n', 'Linha 5\n')
    )

    print('\nFoi escrito no arquivo...')
    print('Seu arquivo será fechado...')

print_division()

with open(file_path, 'r') as file:
    print('LEITURA (r)')
    print(file.read())

    print('Foi lido o arquivo')
    print('Seu arquivo será fechado...')

print_division()

with open(file_path, 'w+') as file:
    print('ESCRITA & LEITURA (w+)')
    file.write('Linha 1.1\n')
    file.write('Linha 2.1\n')
    file.write('Linha 3.1\n')

    print('READ')
    file.seek(0, 0)
    print(file.read())

    print('\nREAD LINE')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline().strip())

    print('\nREAD LINES')
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip())

    print('\nFoi escrito e lido o arquivo...')
    print('Seu arquivo será fechado...')

with open(file_path, 'a+', encoding='utf-8') as file:
    print('ESCRITA & LEITURA SEM APAGAR OS DADOS ANTERIORES (a+)')
    file.write('Linha 1.2\n')
    file.write('Linha 2.2\n')
    file.write('Linha 3.3\n')
    file.write('Atenção')

    print('READ')
    file.seek(0, 0)
    print(file.read())

# Remove o arquivo
# os.remove(file_path)
# os.unlink(file_path)

# Altera o nome do arquivo e pode mover ele
# os.rename(file_path, 'intermediario/aula_118_2.txt')
