"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores

Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
- fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

https://brasilescola.uol.com.br/matematica/fatorial.htm
"""
import sys
sys.setrecursionlimit(1004)

def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')

def print_iterator(name, iterator):
  print(name)
  print(*iterator, sep='\n')

def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')
  
def recursive(start=0, end=10):
  # Contar até chegar ao final
  print(start, end)
  
  if start >= end:
    return end
  
  start += 1
  
  return recursive(start, end)

print('RECURSIVIDADE'.center(50))
print(recursive())

print_division()

def factorial(n):
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)

print('FATORIAL'.center(50))
num = 4
print(f'{num}! = {factorial(num)}')

num = 12
print(f'{num}! = {factorial(num)}')

num = 9
print(f'{num}! = {factorial(num)}')