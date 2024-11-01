"""
Faça um jogo para o usuário adivinhar qual a palavra secreta
- Você vai propor uma palavra secreta e o usuário vai digitar uma letra
- A letra digitada pelo usuário será conferida para ver se está na palavra secreta
- Se a palavra digitada estiver na palavra secreta, exiba a letra
- Se a letra digitada não estiver n a palavra secreta, exiba "*"
- Faça a contagem de tentativas do usuário
"""

import os

palavra_secreta = 'originalidade'
letras_acertadas = ''
tentativas = 0

while True:
  letra_digitada = input('Digite uma letra: ')
  tentativas += 1

  if len(letra_digitada) > 1:
    print('Digite apenas uma letra')
    continue

  if letra_digitada in palavra_secreta:
    letras_acertadas += letra_digitada
  
  palavra_formatada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
      palavra_formatada += letra_secreta
    else:
      palavra_formatada += "*"
  
  print(f"Palavra formada: {palavra_formatada}")

  if (palavra_formatada == palavra_secreta):
    os.system('clear')
    print(f"Parabéns, você acertou a palavra secrata '{palavra_secreta}'!")
    print(f"Você acertou a palavra em {tentativas} tentativas!")

    tentativas = 0;
    letras_acertadas = ''

    input('Pressione enter para jogar novamente')
    os.system('clear')

