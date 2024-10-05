"""
copy, sorted, produtos.sort

Exercícios
- Aumente os preços dos produtos a seguir em 10%

- Gere novos_produtos por deep copy (cópia profunda)

- Ordene os produtos por nome decrescente (do maior para menor)
- Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

- Ordene os produtos por preco crescente (do menor para maior)
- Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
from dados import products

import copy

print('PRODUTOS'.center(50))
print(*products, sep='\n')

print('', '=' * 50, '', sep='\n')

novos_produtos = [
  {**p, 'preco': round(p['preco'] * 1.1, 2)}
  for p in copy.deepcopy(products)
]
  
print('NOVOS PRODUTOS'.center(50))
print(*novos_produtos, sep='\n')

print('', '=' * 50, '', sep='\n')

produtos_ordenados_por_nome = sorted(
  copy.deepcopy(products),
  key=lambda p: p['nome'],
  reverse=True
)

print('ORDENADOS POR NOME'.center(50))
print(*produtos_ordenados_por_nome, sep='\n')

print('', '=' * 50, '', sep='\n')

produtos_ordenados_por_preco = sorted(
  copy.deepcopy(products),
  key=lambda p: p['preco']
)

print('ORDENADOS POR PREÇO'.center(50))
print(*produtos_ordenados_por_preco, sep='\n')