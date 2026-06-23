import json
import os
from transaction import Transaction

from account import SavingAccount

class Bank:

    FILE_NAME = "data.json"

    def __init__(self):
        self.accounts = []
        self.load_accounts()

    def load_accounts(self):

        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME,"r") as file:

                data = json.load(file) 

                for item in data:
                    account  = SavingAccount (
                        item["account_no"],
                        item["name"],
                        item["balance"]
                    )

                    if "transactions" in item:
                        for t in item["transactions"]:
                            transaction = Transaction(t["type"], t["amount"])
                            transaction.date = t["date"]
                            account.transactions.append(transaction)

                    self.accounts.append(account)

    def save_accounts(self):

        data = []    

        for account in self.accounts:
            data.append(account.to_dict())

        with open(self.FILE_NAME,"w") as file:
            json.dump(data,file , indent=4) 

    def create_account(self,account):
        self.accounts.append(account)
        self.save_accounts()

    def find_account(self,account_no):
        for account in self.accounts:

            if account.account_no == account_no:
                return account

        return None                              
