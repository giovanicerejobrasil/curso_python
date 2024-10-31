"""
Implementando o protocolo do Iterator em Python

Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura usada nessa aula.

https://docs.python.org/3/library/collections.abc.html
"""
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self) -> None:
        self._data: dict = {}
        self._index: int = 0
        self._next_index: int = 0

    def append(self, *values) -> None:
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value) -> None:
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    list_ = MyList()
    list_.append('Giovani', 'Luanna', 'Maria')

    print(list_._data)
    print(len(list_))
    list_[2] = 'Mel'
    print(list_[1])
    print()

    for ls in list_:
        print(ls)

    print('-' * 10)

    for ls in list_:
        print(ls)
