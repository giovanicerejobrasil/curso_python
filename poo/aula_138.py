"""
Relações entre classes: associação, agregação e composição

Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.

Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.

(existem controvérsias sobre as definições de agregação).
"""


class Cart:
    def __init__(self) -> None:
        self._products = []

    def insert_products(self, *products):
        self._products.extend(products)

    def total(self):
        return sum([p.price for p in self._products])

    def list_products(self):
        print('LISTA DE PRODUTOS')
        for product in self._products:
            print(f'{product.name} - R$ {product.price:.2f}')


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


cart = Cart()
p1, p2 = Product('Mouse', 39.90), Product('Teclado', 289.99)

cart.insert_products(p1, p2)
cart.list_products()

print_division('VALOR TOTAL DOS PRODUTOS')
print(f'R$ {cart.total():.2f}')
