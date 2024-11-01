"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:.>10}')
print(f'{variavel:.<10}')
print(f'{variavel:.^9}')
print(f'{1000.19959151144164844684:0=+10.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')