"""
Dictionary Comprehension e Set Comprehension
"""

produto = {
  'nome': 'Notebook',
  'preco': 3565.99,
  'categoria': 'Informática',
}

dc = {
  chave: valor.upper()
  if isinstance(valor, str)
  else valor
  for chave, valor
  in produto.items()
  if chave != 'categoria'
}
print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)

print(set(range(10)))