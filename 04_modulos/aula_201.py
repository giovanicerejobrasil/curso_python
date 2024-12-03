"""
Deque - Trabalhando com LIFO e FIFO
deque - Double-ended queue

Lifo  e fifo
pilha e fila

LIFO (Last In First Out)
Pilha (stack)
Significa que o último item a entrar será o primeiro a sair (list)

Artigo:
https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/

Vídeo:
https://youtu.be/svWVHEihyNI

Para tirar itens do final: O(1) Tempo constante
Para tirar itens do início: O(n) Tempo Linear
"""
from collections import deque


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


print_division(text='lifo with list')
list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Legal (LIFO com lista)

#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_.append(10)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_.append(11)
#  0  1  2  3  4  5  6  7  8  9  10  11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

last_removed = list_.pop()
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Último:', last_removed)
print('Lista:', list_)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()

print_division(text='fifo with list', jump=True)
list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🚫 Ruim (FIFO com lista)

#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_.insert(0, 10)
#   0  1  2  3  4  5  6  7  8  9  10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_.insert(0, 11)
#   0  1  2  3  4  5  6  7  8  9  10  11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_removed = list_.pop(0)  # 11
#   0  1  2  3  4  5  6  7  8  9  10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Primeiro:', first_removed)
print('Lista:', list_)

print()

"""
FIFO (First In First Out)

Filas (queue)

Significa que o primeiro item a entrar será o primeiro a sair (deque)

Artigo:
https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/

Vídeo:
https://youtu.be/RHb-8hXs3HE

Para tirar itens do final: O(1) Tempo constante
Para tirar itens do início: O(1) Tempo constante
"""

# Legal (FIFO com deque)

print_division(text='fifo with deque', jump=True)

correct_queue: deque[int] = deque()
correct_queue.append(3)  # Adiciona no final
correct_queue.append(4)  # Adiciona no final
correct_queue.append(5)  # Adiciona no final
correct_queue.appendleft(0)  # Adiciona no início
correct_queue.appendleft(1)  # Adiciona no início
correct_queue.appendleft(2)  # Adiciona no início

print(correct_queue)  # deque([2, 1, 0, 3, 4, 5])

right_removed = correct_queue.pop()  # 5
left_removed = correct_queue.popleft()  # 2

print()
print('Removido da direita:', right_removed)
print('Removido da esquerda:', left_removed)
print()

print(correct_queue)  # deque([1, 0, 3, 4])
