"""
Usando calendar para calendários e datas

https://docs.python.org/3/library/calendar.html

Calendar é usado para coisas genéricas de calendários e datas.

Com calendar, você pode saber coisas como:
- Qual o último dia do mês (ex.: monthrange)
- Qual o nome e número do dia de determinada data (ex.: weekday)
- Criar um calendário em si (ex.: monthcalendar)
- Trabalhar com coisas específicas de calendários (ex.: calendar, month)

Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
"""
import calendar


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division(text='CALENDÁRIO DO MÊS - MONTH')
print(calendar.month(2024, 12))

print_division(text='PRIMEIRO E ÚLTIMO DIA DO MÊS - MONTHRANGE')
first_day, last_day = calendar.monthrange(2024, 12)
print((first_day, last_day))
print(list(enumerate(calendar.day_name)))
print('PRIMEIRO DIA:', calendar.day_name[first_day])
print('ÚLTIMO DIA:', calendar.day_name[calendar.weekday(2022, 12, last_day)])

print_division(text='NÚMERO DO DIA DA SEMANA - WEEKDAY')
print('2024-12-31:', calendar.weekday(2024, 12, last_day))

print_division(text='CRIAR UM CALENDÁRIO - MONTHCALENDAR')
for week in calendar.monthcalendar(2024, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
