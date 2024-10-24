"""
super() e a sobreposição de membros - Python Orientado a Objetos

Classe principal (Pessoa)
  -> super class, base class, parent class

Classes filhas (Cliente)
  -> sub class, child class, derived class
"""

# class MyString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         return super().upper()


# string = MyString('Giovani')
# print(string.upper())


class A:
    attribute_a = 'value A'

    def __init__(self, attribute):
        self.atribute = attribute

    def method(self):
        print('A')


class B(A):
    attribute_b = 'value B'

    def __init__(self, attribute, other_attribute):
        super().__init__(attribute)
        self.other_attribute = other_attribute

    def method(self):
        print('B')


class C(B):
    attribute_c = 'value C'

    def __init__(self, *args, **kwargs):
        print('SISTEMA BURLADO')
        super().__init__(*args, **kwargs)

    def method(self):
        # B.method(self)  # B
        super().method()  # B
        # A.method(self)  # A
        super(B, self).method()  # A
        print('C')


def print_division(text='', num_repeat=35, jump_line=False):
    print() if jump_line else ''
    print('=' * num_repeat, sep='\n')
    print(text, end='\n\n')


c = C('ATRIBUTO A', 'ATRIBUTO B')

print_division('ATRIBUTOS', jump_line=True)
print(c.attribute_a)
print(c.attribute_b)
print(c.attribute_c)
print(c.atribute)
print(c.other_attribute)

print_division('MÉTODOS', jump_line=True)
c.method()

print_division('METHOD RESOLUTION ORDER (MRO)', jump_line=True)
print('CLASSE C')
print(*C.mro(), sep='\n', end='\n\n')

print('CLASSE B')
print(*B.mro(), sep='\n', end='\n\n')

print('CLASSE A')
print(*A.mro(), sep='\n')
