"""
Combinations, Permutations e Product - itertools

Combinations - Ordem não importa - iterável + tamanho do grupo

Permutations - Ordem importa

Product - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

def print_iterator(iterator):
  print(*iterator, sep='\n')
  
def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')

people = [
  'Giovani', 'Luanna', 'Mel', 'Malu'
]

tshirts = [
  ['black', 'white'],
  ['P', 'M', 'G'],
  ['Masculino', 'Feminino', 'Unisex'],
  ['Algodão', 'Poliéster']
]

print('COMBINAÇÕES')
print_iterator(combinations(people, 2))

print_division()

print('PERMUTAÇÕES')
print_iterator(permutations(people, 2))

print_division()

print('PRODUTO')
print_iterator(product(*tshirts))
