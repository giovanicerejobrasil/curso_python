"""
Fatiamento de strings
 0   1   2   3   4  5  6  7  8  9 10 11 12
 H   e   l   l   o  ,     W  o  r  l  d  !
-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

Fatiamento [i:f:p] [::]
Obs.: A função len retorna a quantidade de
caracteres da string
"""

variável = "Hello, World!";

print(f"O texto '{variável}' tem o tamanho de {len(variável)} caracteres!")
print(variável[7])
print(variável[7:])
print(variável[4:8])
print(variável[:-8])
print(variável[::2])
print(variável[::-1])