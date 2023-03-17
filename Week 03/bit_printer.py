a = int(input('bit number: '))

if (a < 0 or a > 2):
    print('Invalid bit number')
else:
    if ((0 >> a) & 0b1 == 1):
        print('0')
    
    if ((1 >> a) & 0b1 == 1):
        print('1')
    
    if ((2 >> a) & 0b1 == 1):
        print('2')
    
    if ((3 >> a) & 0b1 == 1):
        print('3')
    
    if ((4 >> a) & 0b1 == 1):
        print('4')
    
    if ((5 >> a) & 0b1 == 1):
        print('5')

    if ((6 >> a) & 0b1 == 1):
        print('6')

    if ((7 >> a) & 0b1 == 1):
        print('7')

# or ...
# mask = 0b001 << a
# if (0 & mask != 0):
#   print(0)