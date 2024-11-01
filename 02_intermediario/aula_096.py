"""
try, except, else e finally
https://docs.python.org/3/library/exceptions.html
"""

try:
  a = 10
  b = 0

  print('INICIO TRY')
  # print(a[0])
  # c = a / b
  # print(c)
  print('FINAL TRY'[1000])
except ZeroDivisionError as error:
  print('ZeroDivisionError:', error)
except NameError as error:
  print('NameError:', error)
except (TypeError, IndexError) as error:
  print(f"{error.__class__.__name__} :", error)
except Exception as error:
  print('Exception:', error)

print('', '=' * 50, '', sep='\n')

try:
  print('TRY')
  # print(8 / 0)
except ZeroDivisionError as error:
  print('EXCEPT')
  print(f"{error.__class__.__name__}: {error}")
else:
  print('ELSE')
finally:
  print('FINALLY')