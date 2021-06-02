from daos.accounts_dao import AccountDAO
from entities.account import Account
from services.account_service import AccountService

class AccountServiceImpl(AccountService):

    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def add_account(self, account: Account):
        return self.account_dao.create_account(account)

    def retrieve_account_by_id(self, account_id: int):
        return self.account_dao.get_account_by_id(account_id)

    def retrieve_all_accounts(self, client_id: int):
        return self.account_dao.get_all_accounts(client_id)

    def retrieve_all_accounts_in_range(self, client_id: int, ceiling: int, floor: int):
        return self.account_dao.get_all_accounts_in_range(client_id, ceiling, floor)

    def update_account(self, account: Account):
        return self.account_dao.update_account(account)

    #At the current time the bank does allow for overdrawing but if that changes we can implement that here
    def withdraw(self, account_id: int, amount: int):
        return self.account_dao.withdraw(account_id, amount)

    def deposit(self, account_id: int, amount: int):
        return self.account_dao.deposit(account_id, amount)

    #This needs fixing too
    def remove_account(self, account_id: int):
        result = self.account_dao.delete_account(account_id)
        if result:
            return result
        else:
            raise ResourceWarning(f"account with id {account_id} could not be found")



