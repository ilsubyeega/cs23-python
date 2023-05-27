class Account:
    MAX_AMOUNT_PER_TRANSACTION = 10000
    def __init__(self, balance = 0):
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > Account.MAX_AMOUNT_PER_TRANSACTION:
            raise ValueError("Amount exceeds the maximum amount per transaction")
        self.balance += amount
    def withdraw(self, amount):
        if amount > Account.MAX_AMOUNT_PER_TRANSACTION:
            raise ValueError("Amount exceeds the maximum amount per transaction")
        if amount > self.balance:
            raise ValueError("Amount exceeds the current balance")
        self.balance -= amount

class IdentifiedAccount(Account):
    def __init__(self, *, id, balance=0):
        super().__init__(balance)
        self.id = id
    def get_id(self):
        return self.id