"""
Introdução às Generators Functions em Python
generator = (n for n in range(1000000))
"""

def generator(n = 0, max = 10, step = 1):
  while True:
    yield n
    n += step
    
    if n >= max:
      return

gen = generator(max = 1000000)

for n in gen:
  print(n)