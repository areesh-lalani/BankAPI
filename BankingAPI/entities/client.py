

class Client:
    def __init__(self, client_id: int, first_name: str, last_name: str):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        #self.accounts = accounts

    def as_json_dict(self):
        return {
            "clientId":self.client_id,
            "firstName":self.first_name,
            "lastName":self.last_name
        }