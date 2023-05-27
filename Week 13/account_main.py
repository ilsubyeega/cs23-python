import account_mod as account
my_acc = account.Account(1000)
my_id_acc = account.IdentifiedAccount(id=134, balance=1000)
my_minus_acc = account.MinusAccount(balance=500, cont_balance=500) # init_balance not found.

my_acc.deposit(500)
print(my_id_acc.get_balance())
my_minus_acc.withdraw(700)