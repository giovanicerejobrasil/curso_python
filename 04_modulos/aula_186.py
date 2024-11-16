"""
string.Template para substituir variáveis em textos
doc: https://docs.python.org/3/library/string.html#template-strings

Métodos:
    - substitute: substitui mas gera erros se faltar chaves
    - safe_substitute: substitui sem gerar erros

Você também pode trocar o delimitador e outras coisas criando uma subclasse
de template.
"""
import json
import locale
import string
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'aula_186.txt'


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def convert_to_brl(number: float) -> str:
    brl = 'R$ ' + locale.currency(val=number, symbol=False, grouping=True)
    return brl


date_ = datetime(2024, 11, 16)
data_ = dict(
    name='Giovani',
    value=convert_to_brl(1_234_567),
    date=date_.strftime('%d/%m/%Y'),
    company='G.B. Development',
    phonenumber='+55 (91) 980247838'
)

print_division('SHOW DATA')
print(json.dumps(data_, indent=2, ensure_ascii=True))


class MyTemplate(string.Template):
    delimiter = '%'


with open(FILE_PATH, 'r') as file:
    text = file.read()
    template = MyTemplate(text)

    print_division('STRING TEMPLATE SUBSTITUTE', jump=True)
    print(template.substitute(data_))
