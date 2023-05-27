from utility.account import Account

acc = Account()
acc.deposit(999)
try:
    acc.deposit(10001)
except ValueError:
    print('transaciton limit over or low balance')
print(acc.balance)