import accounts


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._name!r}, {self._age!r})'
        return f'{class_name}{attrs}'


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None


if __name__ == '__main__':
    client_1 = Client('Giovani', 27)
    client_1.account = accounts.CheckingAccount(122, 222)
    print(client_1)
    print(client_1.account)

    print('', '#' * 40, '', sep='\n')

    client_2 = Client('Luanna', 24)
    client_2.account = accounts.SavingAccount(366, 333, 100)
    print(client_2)
    print(client_2.account)
