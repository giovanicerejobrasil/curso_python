"""
For + range
range -> range (start, stop, step)
"""

texto = 'Giovani Cerejo Brasil'

for t in range(0, len(texto), 2):
  print(f"{t} => {texto[t]}")
