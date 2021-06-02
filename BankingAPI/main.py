from flask import Flask, request, jsonify
from daos.client_dao import ClientDao
from daos.accounts_dao import AccountDAO
from daos.client_dao_postgres import ClientDaoPostgres
from daos.account_dao_postgres import AccountDaoPostgres
from entities.client import Client
from entities.account import Account
from services.client_service import ClientService
from services.account_service import AccountService
from services.client_service_impl import ClientServiceImpl
from services.account_service_impl import AccountServiceImpl
from exceptions.not_found_exception import ResourceNotFoundError
import logging

app: Flask = Flask(__name__)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

client_dao: ClientDao = ClientDaoPostgres()
client_service: ClientService = ClientServiceImpl(client_dao)

account_dao: AccountDAO = AccountDaoPostgres()
account_service: AccountService = AccountServiceImpl(account_dao)



#come back and remove clientId from this
@app.route("/clients", methods=["POST"])
def create_client():
    body = request.json
    #print(str(body))
    client = Client(0, body["firstName"], body["lastName"])
    client_service.add_client(client)
    return f"Created client with id{client.client_id}", 201


@app.route("/clients/<client_id>", methods=["GET"])
def get_client_by_id(client_id: str):
    try:
        client = client_service.retrieve_client_by_id(int(client_id))
        return jsonify(client.as_json_dict())
    except TypeError as e:
        return "No client with that Id exists", 404

@app.route("/clients/<client_id>/accounts/<account_id>", methods=["GET"])
def get_account_by_id(client_id: str, account_id: str):
    try:
        account = account_service.retrieve_account_by_id(int(account_id))
        return jsonify(account.as_json_dict())
    except TypeError as e:
        return "No account with that Id exists", 404

@app.route("/clients", methods=["GET"])
def get_all_clients():
    clients = client_service.retrieve_all_clients()
    json_clients = [c.as_json_dict() for c in clients]
    return jsonify(json_clients)

@app.route("/clients/<client_id>", methods=["PUT"])
def update_client(client_id: str):
    body = request.json
    client = Client(body["clientId"], body["firstName"], body["lastName"])
    client.client_id = int(client_id)
    client_service.update_client(client)
    return "client update successful"


@app.route("/clients/<client_id>", methods=["DELETE"])
def remove_client(client_id: str):
    try:
        client_service.remove_client(int(client_id))
        return "client successfully deleted", 200
    except ResourceNotFoundError:
        return f"no client with {client_id} found", 404

@app.route("/clients/<client_id>/accounts", methods=["POST"])
def create_account(client_id: str):
    body = request.json
    # print(str(body))
    account = Account(0, body["amount"], client_id)
    account_service.add_account(account)
    return f"Created account with id{account.account_id}", 201

@app.route("/clients/<client_id>/accounts", methods=["GET"])
def get_all_accounts(client_id: str):
    accounts = account_service.retrieve_all_accounts(int(client_id))
    json_accounts = [a.as_json_dict() for a in accounts]
    return jsonify(json_accounts)

@app.route("/clients/<client_id>/accounts?amountLessThan=<ceiling>&amountGreaterThan<floor>", methods=["GET"])
def get_accounts_in_range(client_id:str, ceiling: str, floor: str):
    accounts = account_service.retrieve_all_accounts(int(client_id), int(ceiling), int(floor))
    json_accounts = [a.as_json_dict() for a in accounts]
    return jsonify(json_accounts)

@app.route("/clients/<client_id>/accounts/<account_id>", methods=["PUT"])
def update_account(client_id: str, account_id: str):
    body = request.json
    account = Account(int(account_id), body["amount"], int(client_id))
    account.account_id = int(account_id)
    account_service.update_account(account)
    return "account update successful"

@app.route("/clients/<client_id>/accounts/<account_id>", methods=["DELETE"])
def delete_account(client_id: str, account_id: str):
    try:
        account_service.remove_account(int(account_id))
        return "account successfully deleted", 205
    except ResourceNotFoundError:
        return f"no account with {account_id} found", 404

@app.route("/clients/<client_id>/accounts/<account_id>", methods=["PATCH"])
def withdraw_deposit(client_id: str, account_id: str):
    body = request.json
    if "withdraw" in body:
        amount = body["withdraw"]
        account_service.withdraw(int(account_id), body["withdraw"])
        return f"{amount} dollars withdrawn", 200
    if "deposit" in body:
        amount = body["deposit"]
        account_service.deposit(int(account_id), body["deposit"])
        return f"{amount} dollars deposited", 200
    return "no funds transferred at this time", 404

@app.route("/clients/<client_id>/accounts/<source_id>/transfer/<target_id>", methods=["PATCH"])
def transfer(client_id: str, source_id: str, target_id: str):
    body = request.json
    amount = int(body["amount"])
    account_service.withdraw(int(source_id), amount)
    account_service.deposit(int(target_id), amount)
    return f"successfully transferred {amount} dollars from account {source_id} to account {target_id}", 200


if __name__ == '__main__':
    app.run()