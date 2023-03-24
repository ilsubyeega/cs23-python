n = -1
while True:
    n = int(input('score : '))
    if n >= 0 and n <= 100:
        break
    print('Invalid score. Please re-input the score.')


if n >= 90:
    print('A')
elif n >= 80:
    print('B')
# ...
else:
    print('F')