"""
Formatando datas do datetime

datetime.strftime('DATA', 'FORMATO')

https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


date = datetime(2025, 1, 2, 10, 23, 58)
date = datetime.strptime('2025-01-02 10:23:58', '%Y-%m-%d %H:%M:%S')

print_division(text='FORMATAÇÃO DE DATAS')
print(date.strftime('%d/%m/%Y'))
print(date.strftime('%d/%m/%Y %H:%M'))
print(date.strftime('%d/%m/%Y %H:%M:%S'))
print(type(date.strftime('%Y')))
print('STR =>', date.strftime('%Y'), '| INT => ', date.year)
print('STR =>', date.strftime('%m'), '| INT => ', date.month)
print('STR =>', date.strftime('%d'), '| INT => ', date.day)
print('STR =>', date.strftime('%H'), '| INT => ', date.hour)
print('STR =>', date.strftime('%M'), '| INT => ', date.minute)
print('STR =>', date.strftime('%S'), '| INT => ', date.second)
