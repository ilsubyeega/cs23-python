numbers = list(range(1,11))
numbers[3:0:-1] = [11, 12, 13]
print(numbers)
for n in numbers[::-1]:
    print(n, end=' ')
print()
print(numbers[2:2:-1])
print(numbers[2:1:-1])