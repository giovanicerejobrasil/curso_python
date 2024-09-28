"""
Empacotamento e desempacotamento de dicionários
"""

a, b = 1, 2
a, b = b, a
print(a, b, end='\n\n')

pessoa = {
  'nome': 'Giovani',
  'sobrenome': 'Brasil'
}

a, b = pessoa
print(a, b, end='\n\n')

a, b = pessoa.values()
print(a, b, end='\n\n')

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2, end='\n\n')

for chave, valor in pessoa.items():
  print(f'{chave}: {valor}')
print(end='\n\n')

dados_pessoa = {
  'idade': 27,
  'altura': 1.70
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa, end='\n\n')

"""
args e kwargs
args (já vimos)
kwargs - keyword arguments (argumentos nomeados)
"""

def mostrar_argumentos_nomeados(*args, **kwargs):
  print('ITENS NÃO NOMEADOS:', args)
  print('ITENS NOMEADOS:', kwargs, end='\n\n')
  
mostrar_argumentos_nomeados(27, 170, nome='Giovani', sobrenome='Brasil')

mostrar_argumentos_nomeados(**pessoa_completa)