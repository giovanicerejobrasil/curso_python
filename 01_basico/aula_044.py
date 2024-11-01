texto = 'Python'
novo_texto = ''

for letra in texto:
  novo_texto += f'*{letra}'
  print(f'{letra}')

print(f'{novo_texto}*')