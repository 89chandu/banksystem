from transaction import Transaction

class Account:
    def __init__(self,account_no,name,balance=0):
        self.account_no = account_no
        self.name = name
        self.__balance = balance
        self.transactions = []

    def _ensure_balance(self):
        if not hasattr(self, "_Account__balance"):
            self.__balance = getattr(self, "balance", 0)

    def deposit(self,amount):
        self._ensure_balance()

        if amount > 0:
            self.__balance += amount

            transaction = Transaction(
                "Deposit",
                amount
            )

            self.transactions.append(transaction)
            return True
        
        return False

    def withdraw(self,amount):
        self._ensure_balance()

        if 0 < amount <= self.__balance :
            self.__balance -= amount

            transaction = Transaction(
                "Withdraw",
                amount
            )

            self.transactions.append(transaction)


            return True

        return False    
    
    def get_balance(self):
        self._ensure_balance()
        return self.__balance
    
    def to_dict(self):

        return {
            "account_no":self.account_no,
            "name":self.name,
            "balance":self.get_balance(),
            "transactions": [
                t.to_dict()
                for t in self.transactions
            ]
        }
    

class SavingAccount(Account):
    def __init__(self,account_no,name,balance=0):
        super().__init__(account_no,name,balance)  

class CurrentAccount(Account):
    def __init__(self,account_no,name,balance=0):
        super().__init__(account_no,name,balance)  

    


    


