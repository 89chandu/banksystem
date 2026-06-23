from datetime import datetime

class Transaction:

    def __init__(self,transaction_type,amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):

        return {
            "type":self.transaction_type,
            "amount":self.amount,
            "date":self.date
        }    
        