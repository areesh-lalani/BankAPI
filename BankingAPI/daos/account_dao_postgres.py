from abc import ABC, abstractmethod
from typing import List
from daos.accounts_dao import AccountDAO
from entities.client import Client
from utils.connection_util import connection
from entities.account import Account

class AccountDaoPostgres(AccountDAO):

    def create_account(self, account: Account):
        sql = """insert into account (amount, c_id) values (%s,%s) returning account_id"""
        # print(type(connection)) debug
        cursor = connection.cursor()
        cursor.execute(sql, (0, account.client_id))
        connection.commit()
        a_id = cursor.fetchone()[0]
        account.account_id = a_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = """select * from account where account_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        record = cursor.fetchone()
        account = Account(record[0], record[1], record[2])
        return account

    def get_all_accounts(self, client_id: int):
        sql = """select * from account where c_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account_list.append(Client(*record))
        return account_list

    def get_all_accounts_in_range(self, client_id: int, ceiling: int, floor: int):
        sql = """select * from account where c_id = %s AND (amount <= %s AND amount >= %s)"""
        cursor = connection.cursor()
        cursor.execute(sql, (client_id, ceiling, floor))
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account_list.append(Client(*record))
        return account_list

    def update_account(self, account: Account):
        sql = """update account set amount=%s where account_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account.amount, account.account_id])
        connection.commit()
        return account

    def withdraw(self, account_id: int, amount: int):
        sql = """update account set amount = amount - %s where account_id = %s returning amount"""
        cursor = connection.cursor()
        cursor.execute(sql, (amount, account_id))
        connection.commit()
        return cursor.fetchone()[0]

    def deposit(self, account_id: int ,amount: int):
        sql = """update account set amount = amount + %s where account_id = %s returning amount"""
        cursor = connection.cursor()
        cursor.execute(sql, (amount, account_id))
        connection.commit()
        return cursor.fetchone()[0] #Allows for easier testing

    def delete_account(self, account_id: int):
        sql = """delete from account where account_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True