

class Account:

    def __init__(self,account_id: int,  amount: int, client_id: int):
        self.account_id = account_id
        self.amount = amount
        self.client_id = client_id

    def withdraw(self, amount: int):
        if amount > self.amount:
            raise ValueError("Error Insufficient Funds")
        self.amount = self.amount - amount

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Please enter a value above 0")
        self.amount = self.amount + amount

    def as_json_dict(self):
        return {
            "accountId": self.account_id,
            "amount": self.amount,
            "clientId": self.client_id
        }

