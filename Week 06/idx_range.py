data = ['good', 'morning', 'hello', 'welcome']
print('data[1:4:1]', data[1:4:1])
print('data, data[::]', data, data[::])
print('data[1:4], data[1:4][0]', data[1:4], data[1:4][0])
print('data[:4]', data[:4])
print('data[1:]', data[1:])
print('data[::2]', data[::2])
print('data[::-1]', data[::-1])
print('data', data)
data[1:3] = 'bye'
print(data)
data[1:3] = ['bye']
print(data)