raw = input('int numbers (seperated by comma ,): ')
data = raw.strip().split(',')

i = 0

for n in data:
    # n = n.strip()
    n = int(n)
    i += n

print('total', i, 'avg', i / len(data))