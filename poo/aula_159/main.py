import one_line
import multiple_lines


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division('DOCSTRING DE UMA LINHA')
print(dir(one_line))
print(one_line.__doc__)
print(one_line.__file__)
print()
print(one_line.__name__)
# help(one_line)

print_division('DOCSTRING DE VÁRIAS LINHAS', jump=True)
print(dir(multiple_lines))
print(multiple_lines.__doc__)
print(multiple_lines.__file__)
print()
print(multiple_lines.__name__)
help(multiple_lines)
