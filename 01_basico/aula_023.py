"""
Operadores in e not in
Strings são iteráveis
 0 1 2 3 4 5 6
 G i o v a n i
-7-6-5-4-3-2-1
"""

nome = "Giovani"

print(nome[3])
print(nome[-5])
print('=' * 20)
print('a' in nome)
print('vaa' in nome)
print('oig' not in nome)
print('o' not in nome)
print('=' * 20)

nome = input("Digite seu nome: ")
encontrar = input("O que deseja encontrar: ")

if encontrar in nome:
  print(f"'{encontrar}' está em {nome}")
else:
  print(f"'{encontrar}' não está em {nome}")