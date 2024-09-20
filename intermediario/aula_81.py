"""
Exercício
Sistema de perguntas e respostas
"""
import os

ESCOLHA_OP = 'Escolha uma opção: ';

perguntas = [
  {
    'pergunta': 'Quanto é 2 + 2?',
    'opcoes': ['1', '3', '4', '5'],
    'resposta': '4'
  },
  {
    'pergunta': 'Quanto é 5 * 5?',
    'opcoes': ['25', '55', '10', '51'],
    'resposta': '25'
  },
  {
    'pergunta': 'Quanto é 10 / 2?',
    'opcoes': ['4', '5', '2', '1'],
    'resposta': '5'
  }
]

estagio = 0
while True:
  if estagio == 0:
    print('Bem vindo ao jogo, Perguntas e Respostas')
    print('[e] - Entrar')
    print('[s] - Sair')
    escolha = input(ESCOLHA_OP)

    if escolha.lower() == 's':
      break

    if escolha.lower() == 'e':
      estagio = 1
    
    os.system('clear')
    
  if estagio == 1:
    pontuacao = 0
    for pergunta in perguntas:
      acertou = False
      print(f'Pergunta: {pergunta['pergunta']}')
      
      opcoes = pergunta['opcoes']

      for key, opcao in enumerate(opcoes):
        print(f'[{key}] {opcao}')

      escolha = input(ESCOLHA_OP)
      
      if escolha.isdigit():
        escolha = int(escolha)
        qtd_opcoes = len(opcoes)

        if escolha < qtd_opcoes and escolha >= 0:
          if pergunta['opcoes'][escolha] == pergunta['resposta']:
            acertou = True
          
      if acertou:
        pontuacao += 1
        print("Parabéns, você acertou! ✅ \n")
      else:
        print('Que pena, você errou! ❌\n')

    print(f'Você acertou {pontuacao} {'questão' if pontuacao == 1 else 'questões'}!')

    if pontuacao <= 1:
      print('Precisa melhorar! 😥\n')
    else:
      print('Parabéns! 🥳🥳🥳\n')
    
    estagio = 0