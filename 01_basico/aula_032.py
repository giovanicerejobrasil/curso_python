"""
Perguntar a hora
Exibir uma saudação a partir:
Bom dia (0 - 11), Boa tarde (12 - 17) e Boa noite (18 - 23)
"""

hora = input('Que horas são?(Ex.: 21) ')

if hora.isdigit():
  hora_int = int(hora)
  
  if hora_int >= 0 and hora_int <= 11:
    print(f'Bom dia! São {hora}h!')
  elif hora_int >= 12 and hora_int <= 17:
    print(f'Boa tarde! São {hora}h!')
  elif hora_int >= 18 and hora_int <= 23:
    print(f'Boa noite! São {hora}h!')
  else:
    print('Horário digitado inexistente')

else:
  print(f'O valor "{hora}" não é um número ou não é um número inteiro')