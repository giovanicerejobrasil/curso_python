"""
reduce - faz a redução de um iterável em um valor
"""
from dados.produtos_module import products
from functools import reduce

def print_iterator(name, iterator):
  print(name)
  print(*iterator, sep='\n')

def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')
  
def reduce_function(accumulator, item):
  return round(accumulator + item['price'], 2)

total_price = reduce(
  reduce_function,
  products,
  0
)
 
total_price = reduce(
  lambda acc, item: round(acc + item['price'], 2),
  products,
  0
) 
 
print_iterator('PRODUTOS', products)
print_division()

print('VALOR TOTAL')
print(f'R$ {total_price:.2f}')