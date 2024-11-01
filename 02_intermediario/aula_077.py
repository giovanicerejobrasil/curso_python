"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
  def saudar(nome):
    return f'{saudacao}, {nome}!'
  return saudar

retornar_bom_dia = criar_saudacao('Bom dia')
retornar_boa_noite = criar_saudacao('Bom noite')

print(retornar_bom_dia('Giovani'))
print(retornar_boa_noite('Luanna'))

for nome in ('Mel', 'Alex', 'Malu'):
  print(retornar_bom_dia(nome))
  print(retornar_boa_noite(nome))