total = 0
for val in range(10):
    if val % 2 == 0:
        continue
    total += val
print(total)