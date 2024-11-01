"""
Exemplo de uso de Dunder Methods (Métodos Mágicos)

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
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point(new_x, new_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y

        return result_self > result_other


if __name__ == '__main__':
    p1 = Point(4, 2)
    p2 = Point(6, 4)
    p3 = p1 + p2

    print(p3)

    print('P1 é maior que P2', p1 > p2)
    print('P2 é maior que P1', p2 > p1)
