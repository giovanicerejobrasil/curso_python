"""
Encapsulamento (modificadores de acesso: public, protected, private)

Python NÃO TEM modificadores de acesso

Mas podemos seguir as seguintes convenções
  (sem underline) = public
  	pode ser usado em qualquer lugar

_ (um underline) = protected
    não DEVE ser usado fora da classe ou suas subclasses.

__ (dois underlines) = private
    "name mangling" (desfiguração de nomes) em Python _NomeClasse__nome_attr_ ou _method só DEVE ser usado na classe em que foi declarado.
"""


class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def public_method(self):
        return 'public_method'

    def _protected_method(self):
        return '_protected_method'

    def __private_method(self):
        return '__private_method'


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


f = Foo()

print_division(text='PUBLIC')

print(f.public)
print(f.public_method())

print_division(text='PROTECTED')

# Sendo usado apenas como exemplo, não é para utilizar desta forma
print(f._protected)
print(f._protected_method())

print_division(text='PRIVATE')

# Sendo usado apenas como exemplo, não é para utilizar desta forma
print(f._Foo__private)
print(f._Foo__private_method())
