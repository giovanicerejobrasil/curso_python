"""
@property + @setter - getter e setter no modo Pythônico

Atributos que começam com um ou dois underlines não devem ser usados fora da classe
"""


class Pen:
    def __init__(self, color):
        self.color = color
        self._cover_color = None

    @property
    def color(self):
        print('PROPERTY')
        return self._color

    @color.setter
    def color(self, color):
        if color == 'Green':
            raise ValueError('Essa cor nã é aceita!')
        print('SETTER', color, sep='\n')
        self._color = color

    @property
    def cover_color(self):
        return self._cover_color

    @cover_color.setter
    def cover_color(self, color):
        self._cover_color = color


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


print_division('PROPERTY AND SETTER')

pen = Pen('Red')
pen.color = 'Pink'
pen.cover_color = 'Orange'

print(pen.color)
print(pen.cover_color)
