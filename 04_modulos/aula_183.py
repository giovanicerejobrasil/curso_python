"""
csv.writer e csv.DictWriter para escrever em CSV

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


CSV_PATH_1 = Path(__file__).parent / 'aula_183_list_dict.csv'
client_list = [
    {'Nome': 'Giovani Brasil', 'Endereço': 'Rua A, "123"'},
    {'Nome': 'Luanna Paixão', 'Endereço': 'Av. C, 456'},
    {'Nome': 'Mel', 'Endereço': 'Rua B, 789'},
    {'Nome': 'Malu', 'Endereço': 'Av. D, 147'},
]

print_division(text="LIST DICTORARY CSV (WRITER | WRITEROW)")
with open(CSV_PATH_1, 'w') as file:
    columns_name_1 = client_list[0].keys()
    writer_1 = csv.writer(file)

    writer_1.writerow(columns_name_1)

    for client_1 in client_list:
        print(client_1)
        writer_1.writerow(client_1.values())

print('\nFINALIZADO COM SUCESSO...')

CSV_PATH_2 = Path(__file__).parent / 'aula_183_list.csv'
client_list_2 = [
    ['Giovani Brasil', 'Rua A, 123'],
    ['Luanna Paixão', 'Av. C, "456"'],
    ['Mel', 'Rua B, 789'],
    ['Malu', 'Av. D, 147'],
]

print_division(text="LIST CSV (WRITER | WRITEROW)", jump=True)
with open(CSV_PATH_2, 'w') as file:
    columns_name_2 = ['Nome', 'Endereço']
    writer_2 = csv.writer(file)

    writer_2.writerow(columns_name_2)

    for client_2 in client_list_2:
        print(client_2)
        writer_2.writerow(client_2)

print('\nFINALIZADO COM SUCESSO...')

CSV_PATH_3 = Path(__file__).parent / 'aula_183_dict.csv'
client_list_3 = [
    {'Nome': 'Giovani Brasil', 'Endereço': 'Rua A, "123"'},
    {'Nome': 'Luanna Paixão', 'Endereço': 'Av. C, 456'},
    {'Nome': 'Mel', 'Endereço': 'Rua B, 789'},
    {'Nome': 'Malu', 'Endereço': 'Av. D, 147'},
]

print_division(
    text="DICTONARY CSV (DICTWRITER | WRITEHEADER | WRITEROW)", jump=True)
with open(CSV_PATH_3, 'w') as file:
    columns_name_3 = client_list_3[0].keys()
    writer_3 = csv.DictWriter(
        file,
        fieldnames=columns_name_3
    )
    writer_3.writeheader()

    for client_3 in client_list_3:
        print(client_3)
        writer_3.writerow(client_3)


print('\nFINALIZADO COM SUCESSO...')
