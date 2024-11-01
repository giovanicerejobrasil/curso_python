"""
Pedir o primeiro nome
Se possuir 4 letras ou menos, mostrar:
  "Seu nome é curto"
Se possuir entre 5 e 6 letras, mostrar:
  "Seu nome é normal"
Maior que 6 letras, mostrar:
  "Seu nome é muito grande"
"""

nome = input('Digite seu primeiro nome: ')
nome_len = len(nome)

if nome and nome_len > 1:

  if nome_len <= 4:
    print("Seu nome é curto")
  elif nome_len >= 5 and nome_len <= 6:
    print("Seu nome é normal")
  else:
    print("Seu nome é muito grande")
else:
  print("Por favor, digite um nome válido ou mais de um caractere!")