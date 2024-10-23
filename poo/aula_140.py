"""
Exercício com classes

1 - Crie uma classe Carro (Nome)
2 - Crie uma classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça a ligação entre Carro tem um Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e um Fabricante
Obs.: Um fabricante pode fabricar vários carros

Exiba o nome do carro, motor e fabricante na tela
"""


class Car:
    def __init__(self, name) -> None:
        self._name = name
        self._engine = None
        self._producer = None

    @property
    def name(self):
        return self._name

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, producer):
        self._producer = producer

    def show_car(self):
        return f"Carro: {self._name}\nMotor: {self._engine}\nFabricante: {self._producer}"


class Engine:
    def __init__(self, name) -> None:
        self.name = name


class Producer:
    def __init__(self, name) -> None:
        self.name = name


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


corsa = Car('Corsa')
prisma = Car('Prisma')
uno = Car('Uno Mile')
fiesta_titanium = Car('Fiesta Titanium')
regera = Car('Regera')

engine_1_0 = Engine('1.0')
engine_2_0_flex = Engine('2.0 Flex')
twin_turbo_aluminum_v8 = Engine('Twin Turbo Aluminum V8')

chevrolet = Producer('Chevrolet')
fiat = Producer('Fiat')
ford = Producer('Ford')
koenigsegg = Producer('Koenigsegg')

corsa.engine = engine_1_0.name
corsa.producer = chevrolet.name

prisma.engine = engine_2_0_flex.name
prisma.producer = chevrolet.name

uno.engine = engine_1_0.name
uno.producer = fiat.name

fiesta_titanium.engine = engine_2_0_flex.name
fiesta_titanium.producer = ford.name

regera.engine = twin_turbo_aluminum_v8.name
regera.producer = koenigsegg.name

print_division(corsa.name.upper())
print(corsa.show_car())

print_division(prisma.name.upper())
print(prisma.show_car())

print_division(uno.name.upper())
print(uno.show_car())

print_division(fiesta_titanium.name.upper())
print(fiesta_titanium.show_car())

print_division(regera.name.upper())
print(regera.show_car())
