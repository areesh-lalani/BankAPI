from abc import ABC, abstractmethod
from typing import List

from entities.client import Client
from entities.account import Account

class AccountDAO(ABC):

    @abstractmethod
    def create_account(self, account: Account):
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts(self, client_id: int):
        pass

    @abstractmethod
    def get_all_accounts_in_range(self, client_id: int, ceiling: int, floor: int):
        pass

    @abstractmethod
    def update_account(self, account: Account):
        pass

    @abstractmethod
    def withdraw(self, account_id: int ,amount: int):
        pass

    @abstractmethod
    def deposit(self, account_id: int ,amount: int):
        pass

    @abstractmethod
    def delete_account(self, account_id: int):
        pass

