"""
split e join com list e str
split  - Divide uma string (list)
join   -  Une uma string
strip  - Remove espaços do início e do fim de uma string
rstrip - Remove espaços da direita de uma string
lstrip - Remove espaços da esquerda de uma string
"""

frase = '   Olha só que coisa    , interessante!'
lista_frases_cruas = frase.split(',')
lista_frases_corrigidas = []

print(frase)
print(lista_frases_cruas)

for i, frase in enumerate(lista_frases_cruas):
  lista_frases_corrigidas.append(lista_frases_cruas[i].strip())

print(lista_frases_corrigidas)

frases_unidas = ', '.join(lista_frases_corrigidas)

print(frases_unidas)