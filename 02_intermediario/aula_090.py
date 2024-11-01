"""
isinstance - para saber se o objeto é de um determinado tipo
"""

lista = [
  'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Giovani'}
]

for item in lista:
  if isinstance(item, set):
    print('SET')
    item.add(5)
    print(item)
    
  if isinstance(item, str):
    print('STR')
    print(item.upper())
    
  if isinstance(item, (int, float)):
    print('NUM')
    print(item, item * 2)