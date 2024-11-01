"""
Relações entre classes: associação, agregação e composição

Composição é uma especialização da agregação.

Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.
"""


class Client:
    def __init__(self, name) -> None:
        self.name = name
        self.addresses = []

    def insert_address(self, street, number):
        self.addresses.append(Address(street, number))

    def insert_external_address(self, address):
        self.addresses.append(address)

    def list_address(self):
        for address in self.addresses:
            print(f'{address.street}, {address.number}')

    def __del__(self):
        print('APAGANDO,', self.name)


class Address:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number

    def __del__(self):
        print('APAGANDO,', self.street + ',', self.number)


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


client = Client('Giovani')
client.insert_address('Rua A', 123)
client.insert_address('Rua B', 456)
client.insert_address('Rua C', 789)

external_address = Address('Rua Externa', 15937)
client.insert_external_address(external_address)

print_division(f'LISTA DE ENDEREÇOS DO CLIENTE: {client.name}')
client.list_address()


print()

del client

print_division('O CÓDIGO TERMINOU')
