"""
Variáveis livres + nonlocal
"""
print('GLOBALS'.center(20))
print(*globals().items(), sep='\n')

print('', '*' * 20, '', sep='\n')

def outside(x):
  a = x
  def inside():
    print(locals())
    return a
  return inside

inside_1 = outside(10)
inside_2 = outside(20)

print('LOCALS'.center(20))
print(inside_1())
print(inside_2())

print('', '*' * 20, '', sep='\n')

def concat(initial_string):
  final_value = initial_string
  
  def internal(concat_value=''):
    nonlocal final_value
    final_value += concat_value
    
    return final_value
  
  return internal

c = concat('a')
c('b')
c('c')
c('d')
c('e')

print('NONLOCALS'.center(20))
print(c())