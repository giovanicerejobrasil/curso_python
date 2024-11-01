"""
Teoria: python Special Methods, Magic Methods ou Dunder Methods

Dunder = Double Underscore = __dunder__

Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#special-method-names

__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
"""


class Point:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'(x={self.x}, y={self.y})'

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}), z={self.z!r}'


def print_division(text='', sep_text='=', num_repeat=35, jump=False):
    print() if jump else ''
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


p1 = Point(1, 2)
p2 = Point(368, 1299)

print_division(text='__STR__')
print(p1)
print_division(text='__REPR__', jump=True)
print(repr(p2))
print(f'{p2!r}')
