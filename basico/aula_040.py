"""
Iterando strings com while
"""

palavra_texto = input('Digite uma palavra: ')
indice = 0
nova_palavra_texto = ''

if palavra_texto:
  palavra_texto_len = len(palavra_texto)
  while indice < palavra_texto_len:
    nova_palavra_texto += f"*{palavra_texto[indice]}"

    indice+=1
  
  print(f'A palavra ou o texto "{palavra_texto}" tem {palavra_texto_len} letras')
  print(f"{nova_palavra_texto}*")
else:
  print('Digite uma palavra válida')