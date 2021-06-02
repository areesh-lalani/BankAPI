from abc import ABC, abstractmethod
from typing import List
from daos.accounts_dao import AccountDAO
from daos.account_dao_postgres import AccountDaoPostgres
from entities.client import Client
from utils.connection_util import connection
from entities.account import Account

account_dao: AccountDAO = AccountDaoPostgres()
test_account = Account(0, 0, 18)

def test_create_account():
    account_dao.create_account(test_account)
    assert test_account.account_id != 0

def test_get_account_by_id():
    account = account_dao.get_account_by_id(test_account.account_id)
    assert test_account.account_id == account.account_id

def test_deposit():
    starting_amount = test_account.amount
    test_account.amount = 5
    assert account_dao.deposit(test_account.account_id, 5) == 5 + starting_amount


def test_withdraw():
    starting_amount = test_account.amount
    assert starting_amount - 1 == account_dao.withdraw(test_account.account_id, 1)

#update this
def test_get_all_accounts():
    accounts = account_dao.get_all_accounts(test_account.client_id)
    assert len(accounts) >= 3

def test_delete_account():
    result = account_dao.delete_account(test_account.account_id)
    assert result