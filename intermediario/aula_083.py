"""
Exemplo de uso dos sets
"""

letras = set()

while True:
  letra = input('Digite: ')

  if letra.lower() == 'sair':
    break

  letras.add(letra.lower())

  if 'l' in letras:
    print('Parabéns')
    break

  print(letras)