cash = int(input("Enter the amount of cash: "))
print("Cash: ", cash)

print("50,000 won:", cash // 50000)
cash = cash % 50000

print("10,000 won:", cash // 10000)
cash = cash % 10000

print("5,000 won:", cash // 5000)
cash = cash % 5000

print("1,000 won:", cash // 1000)