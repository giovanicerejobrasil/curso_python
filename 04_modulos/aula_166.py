"""
# datetime.timedelta e dateutil.relativedelta (calculando datas)

# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


fmt = '%d/%m/%Y %H:%M:%S'
date_start = datetime.strptime('02/01/1997 10:00:00', fmt)
date_end = datetime.strptime('08/07/2025 23:59:59', fmt)

print_division(text='COMPARAÇÃO DE DATAS')
print('date_end > date_start =>', date_end > date_start)
print('date_end < date_start =>', date_end < date_start)
print('date_end === date_start =>', date_end == date_start)

print_division(text='DIFERENÇA ENTRE DATAS')
delta = date_end - date_start
print('FIM - INÍCIO =>', delta)
print()

print(f'DIAS => {delta.days}\n'
      f'SEGUNDOS => {delta.seconds}\n'
      f'MICROSEGUNDOS => {delta.microseconds}')
print('TOTAL DE SEGUNDOS =>', delta.total_seconds())
print()

time_delta = timedelta(days=10, hours=2)
print('FIM + TIMEDELTA(10d, 2h) =>', date_end + time_delta)
print('FIM - TIMEDELTA(10d, 2h) =>', date_end - time_delta)
print()

relative_delta = relativedelta(date_end, date_start)
print('DATA FIM + RELATIVEDELTA(10m, 60s) =>', date_end +
      relativedelta(seconds=60, minutes=10))
print('RELATIVEDELTA(DATA FIM, DATA INICIO) =>', relative_delta)
print('RELATIVEDELTA DIAS =>', relative_delta.days)
print('RELATIVEDELTA ANOS =>', relative_delta.years)
