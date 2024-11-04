"""
Exercício solucionado: calculando as datas e parcelas de um empréstimo

Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada
parcela é no dia 20 de cada mês.

- Crie a data do empréstimo
- Crie a data do final do empréstimo
- Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime
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


total_loan_amount = 1_000_000
delta_years = relativedelta(years=7)
loan_date_start = datetime(2020, 12, 20)
loan_date_end = loan_date_start + delta_years

payment_due_dates = []
due_date = loan_date_start

while due_date < loan_date_end:
    payment_due_dates.append(due_date)
    due_date += relativedelta(months=1)

payment_due_dates_number = len(payment_due_dates)
payment_due_dates_amount = total_loan_amount / payment_due_dates_number

for date in payment_due_dates:
    print(date.strftime('%d/%m/%Y'), f'| R$ {payment_due_dates_amount:,.2f}')

print_division(text='INFORMAÇÕES', jump=True)
print(f'Valor total do empréstimo: R$ {total_loan_amount:,.2f}')
print(f'Número de parcelas em anos: {delta_years.years}')
print(f'Número de parcelas em meses: {payment_due_dates_number}')
print(f'Valor das parcelas: R$ {payment_due_dates_amount:,.2f}')
