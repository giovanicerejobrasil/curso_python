"""
csv.reader e csv.DictReader

csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
"""
import csv
from pathlib import Path


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


CSV_PATH = Path(__file__).parent / 'aula_182.csv'

print_division(text='CSV ABS PATH')
print(CSV_PATH)

print_division(text='CSV READER', jump=True)
with open(CSV_PATH, 'r') as file:
    reader_1 = csv.reader(file)

    for row_1 in reader_1:
        print(row_1)
        print('\n', row_1[0], row_1[1], row_1[2], '\n')

print_division(text='CSV DICTREADER', jump=True)
with open(CSV_PATH, 'r') as file:
    reader_2 = csv.DictReader(file)

    for row_2 in reader_2:
        print(row_2)
        print('\n', row_2['Nome'], row_2['Idade'], row_2['Endereço'], '\n')
