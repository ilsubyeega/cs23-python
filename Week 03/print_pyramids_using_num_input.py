size = int(input('size: '))

for i in range(size):
    print(' ' * (size - i - 1), '*' * (2 * i + 1), sep='')