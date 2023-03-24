total = 0
for _ in range(5):
    while True:
        n = int(input('score : '))
        if n >= 0 and n <= 100:
            break
        print('Invalid score. Please re-input the score.')
    total += n
print(total)