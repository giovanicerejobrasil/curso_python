"""
@property - um getter no modo Pythônico

getter - um método para obter um atributo
cor -> get_cor()

modo pythônico - modo do Python de fazer coisas

@property é uma propriedade do objeto, ela é um método que se comporta como um atributo 🤯 🤯 🤯

Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
"""


# Código cliente - é o código que usa seu código
class Pen:
    def __init__(self, color):
        self.tint_color = color

    def get_color(self):
        print('GET COLOR')
        return self.tint_color

    @property
    def color(self):
        print('PROPERTY')
        return self.tint_color


def print_division(text='', num_repeat=35):
    print('', '=' * num_repeat, sep='\n')
    print(text, end='\n\n')


pen = Pen('Black')

print_division('GET')

print(pen.get_color())
print(pen.get_color())
print(pen.get_color())
print(pen.get_color())

print_division('PROPERTY')

print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
