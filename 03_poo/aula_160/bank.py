import accounts
import people


class Bank:
    def __init__(
        self,
        bank_branches: list[int] | None = None,
        clients: list[people.Client] | None = None,
        accounts: list[accounts.Account] | None = None
    ) -> None:
        self._bank_branches = bank_branches or []
        self._clients = clients or []
        self._accounts = accounts or []

    def _check_bank_branch(self, account: accounts.Account) -> bool:
        if account._bank_branch not in self._bank_branches:
            return False
        return True

    def _check_client(self, client: people.Client) -> bool:
        if client not in self._clients:
            return False
        return True

    def _check_account(self, account: accounts.Account) -> bool:
        if account not in self._accounts:
            return False
        return True

    def _check_client_and_account(
        self,
        client: people.Client,
        account: accounts.Account
    ):
        if account is not client.account:
            return False
        return True

    def authenticate(
        self,
        client: people.Client,
        account: accounts.Account
    ) -> bool:
        return self._check_bank_branch(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_client_and_account(client, account)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._bank_branches!r},'\
            f'{self._clients!r}, {self._accounts!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    client_1 = people.Client('Giovani', 27)
    client_account_1 = accounts.CheckingAccount(123, 222)
    client_1.account = client_account_1

    client_2 = people.Client('Luanna', 24)
    client_account_2 = accounts.SavingAccount(456, 333, 100)
    client_2.account = client_account_2

    bank = Bank()
    bank._bank_branches.extend([123, 456])
    bank._clients.extend([client_1, client_2])
    bank._accounts.extend([client_account_1, client_account_2])

    if bank.authenticate(client_1, client_account_1):
        client_account_1.deposit(50)
        client_account_1.deposit(25)
        client_account_1.withdraw(70)
        client_account_1.withdraw(45)

    print(bank)
