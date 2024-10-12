"""
Positional-Only Parameters (/) e Keyword-Only Arguments (*)
Controlando a quantidade de argumentos posicionais e nomeados em funções

*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)

🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.

PEP 570 – Python Positional-Only Parameters
https://peps.python.org/pep-0570/

🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.

PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""


def sum_positional(a, b, /, x, y):
    print(a + b + x + y)


def sum_keyword(a, b, /, *, c):
    print(a + b + c)


sum_positional(1, 2, y=3, x=4)
sum_keyword(5, 6, c=7)
