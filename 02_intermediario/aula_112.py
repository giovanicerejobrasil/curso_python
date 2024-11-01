"""
groupby - agrupando valores (itertools)
"""
from itertools import groupby

def print_iterator(iterator):
  print(*iterator, sep='\n')
  
def print_division(num_repeat=50):
  print('', '=' * num_repeat, '', sep='\n')
  
def order(student):
  return student['grade']

students = [
  {'name': 'Giovani', 'grade': 'A'},
  {'name': 'Luanna', 'grade': 'B'},
  {'name': 'Caique', 'grade': 'C'},
  {'name': 'Brenda', 'grade': 'C'},
  {'name': 'Mayara', 'grade': 'A'},
  {'name': 'Daniel', 'grade': 'B'},
  {'name': 'Paulo', 'grade': 'B'},
  {'name': 'Paula', 'grade': 'D'},
  {'name': 'Eduardo', 'grade': 'C'},
]

students_groups = sorted(students, key=order)

groups = groupby(students_groups, key=order)

for key, group in groups:
  print(key)
  print_iterator(group)