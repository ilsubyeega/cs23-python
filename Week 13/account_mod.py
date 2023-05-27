# imported from Week 12\7_5.py
class Account:
    MAX_AMOUNT_PER_TRANSACTION = 10000
    def __init__(self, balance = 0):
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

class IdentifiedAccount(Account):
    def __init__(self, id, balance=0):
        super().__init__(balance)
        self.id = id

class MinusAccount(Account):
    def __init__(self, cont_balance, balance=0):
        self.contract_balance = cont_balance
        super().__init__(balance)