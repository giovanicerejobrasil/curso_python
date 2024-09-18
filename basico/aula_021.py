"""
Operadores lógicos
and (e), or (ou) e not (não)
or - Qualquer condição verdadeira avalia toda
a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro,
a expressão interia será avaliada naquele valor.
São considerados falsy
0 0.0 '' False
Também existe o tipo None que é usado para
represental um não valor
"""

entrada = input('[E] entrar [S] sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
  print('Entrar')
else:
  print('Sair')

# Avaliação de curto circuito
print(False or 1 or True or 0)