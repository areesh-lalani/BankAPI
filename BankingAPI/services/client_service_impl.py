from abc import ABC, abstractmethod
from typing import List
from daos.client_dao import ClientDao
from entities.client import Client
from services.client_service import ClientService

class ClientServiceImpl(ClientService):

    def __init__(self, client_dao: ClientDao):
        self.client_dao = client_dao

    def add_client(self, client: Client):
        return self.client_dao.create_client(client)

    def retrieve_client_by_id(self, client_id: int):
        return self.client_dao.get_client_by_id(client_id)

    def retrieve_all_clients(self):
        return self.client_dao.get_all_clients()

    def update_client(self, client: Client):
        return self.client_dao.update_client(client)

    def remove_client(self, client_id: int):
        result = self.client_dao.delete_client(client_id)
        if result:
           return result
        else:
            raise ResourceWarning(f"client with id {client_id} could not be found")