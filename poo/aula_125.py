"""
Entendendo self em classes Python

Classe - Molde (geralmente sem dados)

Instância da classe (objeto) - Tem os dados

Uma classe pode gerar várias instâncias

Na classe o self é a própria instância
"""


class Car():
    def __init__(self, name):
        # self.name = 'Fusca' # Hard Coded
        self.name = name

    def accelerate(self):
        print(f'O {self.name} está acelerando...')


def print_division(num_repeat=50):
    print('', '=' * num_repeat, '', sep='\n')


fusca = Car('Fusca')
fusca.accelerate()
Car.accelerate(fusca)

print_division()

celta = Car(name='Celta')
celta.accelerate()
Car.accelerate(celta)
