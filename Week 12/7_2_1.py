class Account:
    def __init__(self, balance = 0):
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

class IdentifiedAccount(Account):
    def __init__(self, *, id, balance=0):
        super().__init__(balance)
        self.id = id
    def get_id(self):
        return self.id

my_account = IdentifiedAccount(id=135)
print(my_account.get_id())

# Bump
my_account.deposit(1000)
print(my_account.get_balance())