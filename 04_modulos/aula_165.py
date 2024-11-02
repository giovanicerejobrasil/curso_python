"""
Criando datas com módulo datetime

datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()

Era Unix
https://pt.wikipedia.org/wiki/Era_Unix

datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html

Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

Instalando o pytz
pip install pytz types-pytz
"""
from datetime import datetime
from pytz import timezone


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division(text="DATETIME DATA")
date = datetime(2024, 11, 2)

print(date)

print_division(text="DATETIME DATA E HORA", jump=True)
date = datetime(2024, 11, 2, 12, 23, 42)

print(date)

print_division(text="DATETIME STRPTIME", jump=True)
date_str = '2024-11-2 12:23:42'
date_str_fmt = '%Y-%m-%d %H:%M:%S'
date = datetime.strptime(date_str, date_str_fmt)

date_br = '02/01/1997'
date_br_fmt = '%d/%m/%Y'
date_2 = datetime.strptime(date_br, date_br_fmt)

print(date)
print(date_2)

print_division(text="DATETIME NOW", jump=True)
date = datetime.now()

print(date)

print_division(text="DATETIME TIMEZONES", jump=True)
date = datetime.now(timezone('Asia/Tokyo'))
date_2 = datetime(2024, 11, 2, 12, 23, 42, tzinfo=timezone('Atlantic/Madeira'))

print('TOKYO (DATETIME NOW)')
print(date)

print('\nMADEIRA ISLAND (DATETIME)')
print(date_2)

print_division(text="DATETIME UNIX TIMESTAMP", jump=True)
date = datetime.now()
date_2 = datetime.fromtimestamp(date.timestamp())

print('CONVERTER TO UNIX TIMESTAMP')
print(date.timestamp())

print('\nCONVERTER FROM UNIX TIMESTAMP')
print(date_2)
