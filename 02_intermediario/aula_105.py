"""
Original file line number	Diff line number	Diff line change
Funções decoradoras e decoradores
Decorar = Adicionar / Remover/ Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (Açúcar Sintático)
"""

def create_function(function):
  def inside(*args, **kwargs):
    print('DECORAR')
    
    for arg in args:
      is_string(arg)
    result = function(*args, **kwargs)
    
    print('DECORADO')
    return result
  return inside

@create_function
def invert_string(string):
  print(invert_string.__name__)
  return string[::-1]

def is_string(param):
  if not isinstance(param, str):
    raise TypeError('O parâmetro informado não é uma String')

inverted = invert_string('123')

print(inverted)