"""
importlib e singleton
"""

import importlib

import aula_100_m

print(aula_100_m.variable)

for i in range(10):
  print(i)
  importlib.reload(aula_100_m)
  
print('FIM')