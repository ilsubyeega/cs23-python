# 7.5.2. -> 하고싶은대로 정의하기.
class Account:
    MAX_AMOUNT_PER_TRANSACTION = 10000
    def __init__(self, balance=0):
        self.balance = balance

class IdentifiedAccount(Account):
    def __init__(self, id, balance=0):
        super().__init__(balance)
        self.id = id

class MinusAccount(Account):
    def __init__(self, cont_balance, balance=0):
        self.contract_balance = cont_balance
        super().__init__(balance)

class IdentifiedMinusAccount(MinusAccount, IdentifiedAccount):
    def __init__(self, id, cont_balance, balance=0):
        super().__init__(cont_balance, balance)
        super(MinusAccount, self).__init__(id, balance)

im_account = IdentifiedMinusAccount(90, 1000, 2000)
print(im_account.id, im_account.contract_balance, im_account.balance)