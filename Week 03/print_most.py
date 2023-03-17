"""
num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))
num4 = int(input('num4: '))
num5 = int(input('num5: '))

if (num1 < 0):
    print('num1 is not postive.')
elif (num2 < 0):
    print('num2 is not postive.')
elif (num3 < 0):
    print('num3 is not postive.')
elif (num4 < 0):
    print('num4 is not postive.')
elif (num5 < 0):
    print('num5 is not postive.')
else:
    idx = 0
    most = 0
    while idx < 5:
        if (idx == 0 and num1 > most):
            most = num1
        elif (idx == 1 and num2 > most):
            most = num2
        elif (idx == 2 and num3 > most):
            most = num3
        elif (idx == 3 and num4 > most):
            most = num4
        elif (idx == 4 and num5 > most):
            most = num5

        idx += 1

    print(most)
"""

most = 0
for i in range(0, 5):
    num = -1
    while num < 0:
        num = int(input('num: '))

    if (num > most):
        most = num
print(most)
