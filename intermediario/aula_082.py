"""
Sets - Conjuntos em Python (tipo set)

Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm

Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set
set(iteravel) ou {1, 2, 3}
"""
s1 = set() # vazio
s1 = set('Giovani') # com dado
print(s1, type(s1))

s2 = {'Giovani', 'Luanna'} # com dados
print(s2)

print('\n' + '=' * 50 + '\n')

"""
Sets são eficientes para remover valores duplicados
de iteráveis.
- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos;
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)
"""

s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s1)
print(3 in s1)

for num in s1:
  print(num)

print('\n' + '=' * 50 + '\n')

"""
Métodos úteis:
add, update, clear, discard
"""

s1 = set()
s1.add('Giovani')
s1.add(27)
s1.update(('Hello World!', 2, 3,5))
print(s1)

# s1.clear() # Limpa todo o set
s1.discard('Hello World!')
s1.discard('Giovani')
print(s1)

print('\n' + '=' * 50 + '\n')

"""
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2
print(s3)

s3 = s1 & s2
print(s3)

s3 = s1 - s2
print(s3)

s3 = s2 - s1
print(s3)

s3 = s1 ^ s2
print(s3)
