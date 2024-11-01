"""
Método especial __call__
callable é algo que pode ser executado com parênteses.

Em classes normais, __call__ faz a instância de uma classe "callable".
"""


from typing import Any


class CallMe:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number

    def __call__(self, name) -> Any:
        print(f'Chamando: {name} ({self.phone_number})')
        return 'Chamada realizada...'


call1 = CallMe('94960351')
return_ = call1('Giovani Brasil')
print(return_)
