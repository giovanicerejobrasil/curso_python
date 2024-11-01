"""
Ordem dos decoradores
"""

def decorators_factory(name):
  def functions_factory(function):
    print('DECORADOR:', name)
    
    def nasted(*args, **kwargs):
      result = function(*args, **kwargs)
      final = f'{result} {name}'
      
      return final
    return nasted
  return functions_factory

@decorators_factory(name='QUINTO')
@decorators_factory(name='QUARTO')
@decorators_factory(name='TERCEIRO')
@decorators_factory(name='SEGUNDO')
@decorators_factory(name='PRIMEIRO')
def sum(x, y):
  return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)

# multiplication = decorators_factory()(lambda x, y: x * y)

# ten_times_five = multiplication(10, 5)
# print(ten_times_five)