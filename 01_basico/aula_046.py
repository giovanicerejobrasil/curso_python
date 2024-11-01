"""
Iterável -> str, range, etc.
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'Giovani'
iterador = iter(texto)

while True:
  try:
    print(next(iterador))
  except Exception as e:
    break