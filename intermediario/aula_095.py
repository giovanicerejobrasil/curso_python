"""
Yield From
"""

def gen1():
  print('COMEÇOU O GEN 1')
  yield 1
  yield 2
  yield 3
  print('TERMINOU O GEN 1')

def gen3():
  print('COMEÇOU O GEN 3')
  yield 7
  yield 8
  yield 9
  print('TERMINOU O GEN 3')
  
def gen2(gen=None):
  print('COMEÇOU O GEN 2')
  if gen is not None:
    yield from gen()
  yield 4
  yield 5
  yield 6
  print('TERMINOU O GEN 2')
  
g1 = gen2(gen1)
g3 = gen2(gen3)
g2 = gen2()

for i in g1:
  print(i)

print('=' * 50)  

for i in g3:
  print(i)
  
print('=' * 50)  

for i in g2:
  print(i)