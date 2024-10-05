"""
Decoradores com parâmetros
"""

def decorators_factory(a=None, b=None, c=None):
  print(a, b, c)
  def functions_factory(function):
    print('DECORADORA 1')
    
    def nasted(*args, **kwargs):
      print('ANINHADA')
      
      result = function(*args, **kwargs)
      
      return result
    return nasted
  return functions_factory

@decorators_factory(1, 2, 3)
def sum(x, y):
  return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)

multiplication = decorators_factory()(lambda x, y: x * y)

ten_times_five = multiplication(10, 5)
print(ten_times_five)
