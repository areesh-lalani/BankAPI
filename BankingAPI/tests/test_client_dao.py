from abc import ABC, abstractmethod
from typing import List
from daos.client_dao import ClientDao
from daos.client_dao_postgres import ClientDaoPostgres
from entities.client import Client
from utils.connection_util import connection
from entities.account import Account

client_dao: ClientDao = ClientDaoPostgres()
test_client = Client(0, "areesh", "lalani")

def test_create_client():
    client_dao.create_client(test_client)
    assert test_client.client_id != 0

def test_get_client_by_id():
    client = client_dao.get_client_by_id(test_client.client_id)
    assert test_client.first_name == client.first_name

def test_update_client():
    test_client.first_name = "A GOOD FIRST NAME"
    updated_client = client_dao.update_client(test_client)
    assert updated_client.first_name == test_client.first_name

def test_delete_client():
    result = client_dao.delete_client(test_client.client_id)
    assert result

def test_get_all_clients():
    client1 = Client(0, "adam", "ranieri")
    client2 = Client(0, "mega", "man")
    client3 = Client(0, "terry", "pratchett")
    client_dao.create_client(client1)
    client_dao.create_client(client2)
    client_dao.create_client(client3)
    clients = client_dao.get_all_clients()
    assert len(clients) >= 3