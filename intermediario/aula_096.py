"""
raise - lançando exceções (erros)
https://docs.python.org/3/library/exceptions.html
"""

def divisor_validate(divisor):
  if divisor == 0:
    raise ZeroDivisionError('Você está tentando dividir um número por zero')
  
  return True

def check_int_float(number):
  type_number = type(number)
  
  if not isinstance(number, (float, int)):
    raise TypeError(f'"{number}" deve ser int ou float.', f'"{type_number.__name__}" enviado.')
  
  True

def divide(n, d):
  check_int_float(n)
  check_int_float(d)
  divisor_validate(d)
  
  return n / d

print(divide('8', 0))