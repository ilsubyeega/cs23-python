spaces = '    '
stars = '*********'

for i in range(0, 5):
    print(i, spaces[0:4-i] + stars[0:(1+(i*2))])