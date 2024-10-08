"""
map - para mapear dados
"""
from dados.produtos_module import products as products
from functools import partial
from types import GeneratorType

def print_iterator(iterator):
  print(*iterator, sep='\n')

def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')

def increase_price(price, percent):
  return round(price + (price * (percent / 100)), 2)

def change_product_price(product):
  return {
    **product, 
    'price': increase_ten_percent(product['price'])
  }

increase_ten_percent = partial(
  increase_price,
  percent=10
)

new_products = [
  change_product_price(p)
  for p in products
]

new_products_map = map(
  change_product_price,
  products
)

print('PRODUTOS')
print_iterator(products)

print_division()

print('NOVOS PRODUTOS')
print_iterator(new_products)

print_division()

print('NOVOS PRODUTOS COM MAP')
print_iterator(new_products_map)
print()
print(new_products_map)
print('__iter__ =>', hasattr(new_products_map, '__iter__'))
print('__next__ =>', hasattr(new_products_map, '__next__'))
print('isistance(generator) =>', isinstance(new_products_map, GeneratorType))