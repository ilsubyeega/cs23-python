for i in range(4):
    arr = []
    for j in range(16):
        tmp = j >> i
        if tmp & 0b01:
            arr.append(j)
    print(f'{i} : {arr}')

"""
Or....

for bit_n in range(0, 4):
    mask = 1 << bit_n
    for n in range(1, 16):
        if (n & mask) != 0:
            pass #...
"""