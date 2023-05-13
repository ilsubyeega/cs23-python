class Account:
    name: str
    gender: str
    age: int

    def print(self):
        print(f'Account(name={self.name}, gender={self.gender}, age={self.age})')

account = Account()
account.name = 'John'
account.gender = 'Male'
account.age = 2

account.print()
print(type(account))