"""
https://docs.python.org/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Giovani Brasil'
outra_string = f'{string[:3]}ABC{string[7:]}'
print(string)
print(outra_string)
print(string.upper())
print(string.lower())
print(string.zfill(25))