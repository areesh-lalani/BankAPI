from abc import ABC, abstractmethod
from typing import List

from entities.client import Client
from entities.account import Account

class ClientDao(ABC):

    @abstractmethod
    def create_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def get_client_by_id(self, client_id: int) -> Client:
        pass
    @abstractmethod
    def get_all_clients(self) -> List[Client]:
        pass


    #@abstractmethod
    #def get_all_accounts(self, client: Client) -> List[Account]:
    #    pass

    @abstractmethod
    def update_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def delete_client(self, client_id: int) -> Client:
        pass



