from abc import abstractmethod, ABC
from entities.account import Account

class AccountService(ABC):

    @abstractmethod
    def add_account(self, account: Account):
        pass

    @abstractmethod
    def retrieve_account_by_id(self, account_id: int):
        pass

    @abstractmethod
    def retrieve_all_accounts(self, client_id: int):
        pass
    @abstractmethod
    def update_account(self, account: Account):
        pass

    @abstractmethod
    def withdraw(self, account_id: int, amount: int):
        pass

    @abstractmethod
    def deposit(self, account_id: int, amount: int):
        pass

    @abstractmethod
    def remove_account(self, account_id: int):
        pass