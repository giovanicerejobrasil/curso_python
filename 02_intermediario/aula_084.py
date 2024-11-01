"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação.
Retorne a duplicação sonsiderada.

Requisitos:
  A ordem do número duplicado é considerado a partir da segunda
  ocorrência do número, ou seja, o número duplicado em si.
  Exemplo:
    [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
    [1, 2, 3, 4, 5, 6] -> retorne -1 (não tem duplicados)
  Se não encontrar duplicados na lista, retorne -1
"""

int_list_in_list = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
  [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
  [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
  [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
  [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
  [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
  [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
  [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
  [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
  [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def repeat_items_first_occurrence(list):
  checked_items = set()
  first_duplicated = -1
  
  for item in list_items:
    if item in checked_items:
      first_duplicated = item
      break
      
    checked_items.add(item)
    
  return first_duplicated

for list_items in int_list_in_list:
  print(f'Lista Atual: {list_items}')
  
  result = repeat_items_first_occurrence(list_items)
  
  if result == -1:
    print('Não há items duplicados\n')
    continue

  print(f'Primeira ocorrência duplicada: {result}\n')