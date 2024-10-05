"""
count - iterador infinito (itertools)
"""
from itertools import count

count_1 = count(step=8, start=8)
range_1 = range(8, 100, 8)

print('count_1 (__iter__)', '=>', hasattr(count_1, '__iter__'))
print('count_1 (__next__)', '=>', hasattr(count_1, '__next__'))
print('range_1 (__iter__)', '=>', hasattr(range_1, '__next__'))
print('range_1 (__next__)', '=>', hasattr(range_1, '__next__'))

print()
print('COUNT')
for i in count_1:
  if i >= 100:
    break
  
  print(i)
  
print()
print('RANGE')
for i in range_1:
  print(i)