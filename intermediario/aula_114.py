"""
filter - é um filtro funcional
"""
from dados.produtos_module import products

def print_iterator(name, iterator):
  print(name)
  print(*iterator, sep='\n')

def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')
  
new_products = filter(
  lambda product: product['price'] > 50,
  products
)

print_iterator('PRODUTOS', products)
print_division()

print_iterator('NOVOS PRODUTOS', new_products)