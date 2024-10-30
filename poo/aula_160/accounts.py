import abc


class Account(abc.ABC):
    def __init__(self, 	bank_branch: int, bank_account: int,
                 balance: float = 0) -> None:
        self._bank_branch = bank_branch
        self._bank_account = bank_account
        self._balance = balance

    @abc.abstractmethod
    def withdraw(self, value: float) -> float: ...

    def deposit(self, value: float) -> float:
        self._balance += value
        self._details(f'(DEPÓSITO R$ {value})')
        return self._balance

    def _details(self, msg: str = '') -> None:
        print(f'Seu saldo é de R$ {self._balance:.2f} {msg}')
        print('---')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._bank_branch!r}, {self._bank_account!r}, '\
            f'{self._balance!r})'
        return f'{class_name}{attrs}'


class SavingAccount(Account):
    def withdraw(self, value: float) -> float:
        value_pos_withdraw = self._balance - value

        if value_pos_withdraw >= 0:
            self._balance -= value
            self._details(f'(SAQUE R$ {value})')
            return self._balance

        print('Não foi possível sacar o valor desejado!')
        self._details(f'(SAQUE NEGADO R$ {value})')
        return self._balance


class CheckingAccount(Account):
    def __init__(self, bank_branch: int, bank_account: int, balance: float = 0,
                 limit: float = 0) -> None:
        super().__init__(bank_branch, bank_account, balance)
        self._limit = limit

    def withdraw(self, value) -> float:
        value_pos_withdraw = self._balance - value
        max_limit = -self._limit

        if value_pos_withdraw >= max_limit:
            self._balance -= value
            self._details(f'(SAQUE R$ {value})')
            return self._balance

        print('Não foi possível sacar o valor desejado!')
        print(f'Seu limite atual é de R$ {max_limit:.2f}')
        self._details(f'(SAQUE NEGADO R$ {value})')
        return self._balance

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._bank_branch!r}, {self._bank_account!r}, '\
            f'{self._balance!r}, {self._limit!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    saving_account_1 = SavingAccount(1234, 111)
    saving_account_1.withdraw(20)
    saving_account_1.deposit(50)
    saving_account_1.withdraw(32)
    saving_account_1.withdraw(19)

    print('', '#' * 40, '', sep='\n')

    checking_account = CheckingAccount(1234, 111, 0, 500)
    checking_account.withdraw(20)
    checking_account.deposit(50)
    checking_account.withdraw(32)
    checking_account.withdraw(19)
    checking_account.deposit(25)
    checking_account.withdraw(360)
    checking_account.withdraw(145)
